from typing import List
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy import Engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Base(DeclarativeBase):
    pass

movie_genres_table = Table(
    "movie_genres",
    Base.metadata,
    Column("movie_id", ForeignKey("movie.id"), index = True),
    Column("genre", ForeignKey("genre.id"), index = True),
)

movie_keywords_table = Table(
    "movie_keywords",
    Base.metadata,
    Column("movie_id", ForeignKey("movie.id"), index = True),
    Column("keyword_id", ForeignKey("keyword.id"), index = True),
)

movie_production_companies_table = Table(
    "movie_production_companies",
    Base.metadata,
    Column("movie_id", ForeignKey("movie.id"), index = True),
    Column("production_company_id", ForeignKey("production_company.id"), index = True),
)

movie_production_countries_table = Table(
    "movie_production_countries",
    Base.metadata,
    Column("movie_id", ForeignKey("movie.id"), index = True),
    Column("production_country_id", ForeignKey("production_country.iso_3166_1"), index = True),
)

movie_spoken_languages_table = Table(
    "movie_spoken_languages",
    Base.metadata,
    Column("movie_id", ForeignKey("movie.id"), index = True),
    Column("spoken_language_id", ForeignKey("spoken_language.iso_639_1"), index = True),
)

class Movie(Base):
    __tablename__ = "movie"
    budget: Mapped[int]
    genres: Mapped[List["Genre"]] = relationship(secondary = movie_genres_table, back_populates = "movies")
    homepage: Mapped[str] = mapped_column(String(50))
    id: Mapped[int] = mapped_column(primary_key=True, index = True)
    keywords: Mapped[List["Keyword"]] = relationship(secondary = movie_keywords_table, back_populates = "movies")
    original_language: Mapped[str] = mapped_column(String(2), index = True)
    original_title: Mapped[str] = mapped_column(String(50), index = True)
    overview: Mapped[str]
    popularity: Mapped[float]
    production_companies: Mapped[List["ProductionCompany"]] = relationship(secondary = movie_production_companies_table, back_populates = "movies")
    production_countries: Mapped[List["ProductionCountry"]] = relationship(secondary = movie_production_countries_table, back_populates = "movies")
    release_date: Mapped[str] = mapped_column(String(10))
    revenue: Mapped[int]
    runtime: Mapped[int]
    spoken_languages: Mapped[List["SpokenLanguage"]] = relationship(secondary = movie_spoken_languages_table, back_populates = "movies")
    status: Mapped[str] = mapped_column(String(15), index = True)
    tagline: Mapped[str] = mapped_column(String(100))
    title: Mapped[str] = mapped_column(String(50), index = True)
    vote_average: Mapped[float] = mapped_column(index = True)
    vote_count: Mapped[int]
    cast: Mapped[List["Credit"]] = relationship(back_populates="movie")
    crew: Mapped[List["CrewCredit"]] = relationship(back_populates="movie")

class Genre(Base):
    __tablename__ = "genre"
    id: Mapped[int] = mapped_column(primary_key=True, index = True)
    name: Mapped[str] = mapped_column(String(30), index = True)
    movies: Mapped[List["Movie"]] = relationship(secondary = movie_genres_table, back_populates = "genres")

class Keyword(Base):
    __tablename__ = "keyword"
    id: Mapped[int] = mapped_column(primary_key=True, index = True)
    name: Mapped[str] = mapped_column(String(30), index = True)
    movies: Mapped[List["Movie"]] = relationship(secondary = movie_keywords_table, back_populates = "keywords")

class ProductionCompany(Base):
    __tablename__ = "production_company"
    id: Mapped[int] = mapped_column(primary_key=True, index = True)
    name: Mapped[str] = mapped_column(String(30), index = True)
    movies: Mapped[List["Movie"]] = relationship(secondary = movie_production_companies_table, back_populates = "production_companies")

class ProductionCountry(Base):
    __tablename__ = "production_country"
    iso_3166_1: Mapped[str] = mapped_column(String(2), primary_key=True, index = True)
    name: Mapped[str] = mapped_column(String(30), index = True)
    movies: Mapped[List["Movie"]] = relationship(secondary = movie_production_countries_table, back_populates = "production_countries")

class SpokenLanguage(Base):
    __tablename__ = "spoken_language"
    iso_639_1: Mapped[str] = mapped_column(String(2), primary_key=True, index = True)
    name: Mapped[str] = mapped_column(String(30), index = True)
    movies: Mapped[List["Movie"]] = relationship(secondary = movie_spoken_languages_table, back_populates = "spoken_languages")

class Credit(Base):
    __tablename__ = "credit"
    movie_id: Mapped[int] = mapped_column(ForeignKey("movie.id"), index = True)
    movie: Mapped["Movie"] = relationship(back_populates="cast")
    credit_id: Mapped[str] = mapped_column(String(24), primary_key=True, index = True)
    cast_id: Mapped[int]
    character: Mapped[str] = mapped_column(String(50), index = True)
    order: Mapped[int]
    actor_id: Mapped[int] = mapped_column(ForeignKey("actor.id"), index = True)
    actor: Mapped["Actor"] = relationship()

class Actor(Base):
    __tablename__ = "actor"
    id: Mapped[int] = mapped_column(primary_key=True, index = True)
    gender: Mapped[int] = mapped_column(index = True)
    name: Mapped[str] = mapped_column(String(50), index = True)
    cast: Mapped[List["Credit"]] = relationship(back_populates="actor")

class CrewCredit(Base):
    __tablename__ = "crew_credit"
    movie_id: Mapped[int] = mapped_column(ForeignKey("movie.id"), index = True)
    movie: Mapped["Movie"] = relationship(back_populates="crew")
    department: Mapped[str] = mapped_column(String(50), index = True)
    credit_id: Mapped[str] = mapped_column(String(24), primary_key=True, index = True)
    person_id: Mapped[int] = mapped_column(ForeignKey("crew_person.id"), index = True)
    person: Mapped["CrewPerson"] = relationship()
    job: Mapped[str] = mapped_column(String(50), index = True)

class CrewPerson(Base):
    __tablename__ = "crew_person"
    id: Mapped[int] = mapped_column(primary_key=True, index = True)
    gender: Mapped[int] = mapped_column(index = True)
    name: Mapped[str] = mapped_column(String(50), index = True)
    crew: Mapped[List["CrewCredit"]] = relationship(back_populates="person")

def init_engine_schema(engine: Engine):
    Base.metadata.create_all(engine)