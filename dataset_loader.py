from typing import TypeVar, Callable, List
from sqlalchemy import Engine
from sqlalchemy.orm import Session
from sql_types import Movie, Genre, Keyword, ProductionCompany, ProductionCountry, SpokenLanguage, Credit, Actor, CrewCredit, CrewPerson, init_engine_schema
from sqlalchemy import create_engine
import logging
import json
import csv
import zipfile
import io
import os

DATASETS_ARCHIVE = "datasets.zip"
MOVIES_DATASET_FILE = "tmdb_5000_movies.csv"
CREDITS_DATASET_FILE = "tmdb_5000_credits.csv"
DATABASE_FILE = "tmdb_5000.db"

logger = logging.getLogger(__name__)

def make_movie(row: dict[str, str]):
    T = TypeVar("T")

    def make_genre(genre_dict: dict) -> Genre:
        return Genre(id = genre_dict["id"], name = genre_dict["name"])
    
    def make_keyword(kw_dict: dict) -> Keyword:
        return Keyword(id = kw_dict["id"], name = kw_dict["name"])
    
    def make_production_company(comp_dict: dict) -> ProductionCompany:
        return ProductionCompany(id = comp_dict["id"], name = comp_dict["name"])
    
    def make_production_country(country: dict) -> ProductionCountry:
        return ProductionCountry(iso_3166_1 = country["iso_3166_1"], name = country["name"])
    
    def make_spoken_language(lang_dict: dict) -> SpokenLanguage:
        return SpokenLanguage(iso_639_1 = lang_dict["iso_639_1"], name = lang_dict["name"])
    
    def get_json(entry_name: str):
        return json.loads(row[entry_name])
    
    def get_json_list(factory: Callable[[dict], T], entry_name: str) -> List[T]:
        return list(map(factory, get_json(entry_name)))
    
    movie = Movie(
        budget = int(row["budget"]),
        genres = get_json_list(make_genre, "genres"),
        homepage = row["homepage"],
        id = int(row["id"]),
        keywords = get_json_list(make_keyword, "keywords"),
        original_language = row["original_language"],
        original_title = row["original_title"],
        overview = row["overview"],
        popularity = float(row["popularity"]),
        production_companies = get_json_list(make_production_company, "production_companies"),
        production_countries = get_json_list(make_production_country, "production_countries"),
        release_date = row["release_date"],
        revenue = int(row["revenue"]),
        runtime = int(float(row["runtime"] or 0.0)),
        spoken_languages = get_json_list(make_spoken_language, "spoken_languages"),
        status = row["status"],
        tagline = row["tagline"],
        title = row["title"],
        vote_average = float(row["vote_average"]),
        vote_count = int(row["vote_count"])
    )

    return movie

def put_movie_row(engine: Engine, row: dict[str, str]):
    with Session(engine) as session:
        session.merge(make_movie(row))
        session.commit()

def put_credit_row(engine: Engine, row: dict[str, str]):
    def make_actor(row: dict) -> Actor:
        return Actor(id = row["id"], gender = row["gender"], name = row["name"])
    
    def make_credit(mov_id: int, row: dict) -> Credit:
        return Credit(movie_id = mov_id, credit_id = row["credit_id"], character = row["character"], order = row["order"], cast_id = row["cast_id"], actor = make_actor(row))
    
    def make_crew_person(row: dict) -> CrewPerson:
        return CrewPerson(id = row["id"], gender = row["gender"], name = row["name"])
    
    def make_crew_credit(mov_id: int, row: dict) -> CrewCredit:
        return CrewCredit(movie_id = mov_id, credit_id = row["credit_id"], department = row["department"], job = row["job"], person = make_crew_person(row))

    def get_json(entry_name: str):
        return json.loads(row[entry_name])
    
    with Session(engine) as session:
        movie_id = int(row['movie_id'])

        entities = []
        entities.extend(make_credit(movie_id, cred) for cred in get_json("cast"))
        entities.extend(make_crew_credit(movie_id, cred) for cred in get_json("crew"))

        for entity in entities:
            session.merge(entity)
        
        session.commit()
        

def load_movies_to_engine(archive: zipfile.ZipFile, engine: Engine):
    with archive.open(MOVIES_DATASET_FILE, 'r') as movies_csv:
        movies_csv_text = io.TextIOWrapper(movies_csv, encoding = 'utf-8')
        movies_reader = csv.DictReader(movies_csv_text)
        for mov in movies_reader:
            put_movie_row(engine, mov)

def load_credits_to_engine(archive: zipfile.ZipFile, engine: Engine):
    with archive.open(CREDITS_DATASET_FILE, 'r') as credits_csv:
        credits_csv_text = io.TextIOWrapper(credits_csv, encoding = 'utf-8')
        credits_reader = csv.DictReader(credits_csv_text)
        for credits in credits_reader:
            put_credit_row(engine, credits)

def load_data_to_engine(engine: Engine):
    with zipfile.ZipFile(DATASETS_ARCHIVE) as archive:
        load_movies_to_engine(archive, engine)
        load_credits_to_engine(archive, engine)

def open_db() -> Engine:
    logging.info("Opening DB SQLAlchemy engine.")
    initialized = os.path.exists(DATABASE_FILE)
    engine = create_engine(f"sqlite+pysqlite:///{DATABASE_FILE}")

    if not initialized:
        logging.info("There wasn't DB. Let's create and fill new schema.")
        init_engine_schema(engine)
        load_data_to_engine(engine)
    
    return engine