from typing import List, Optional
from sqlalchemy import select
from sqlalchemy.orm import Session
from strawberry.types import Info
import strawberry
import sql_types

GENDER_FEMALE_ID = 1
GENDER_MALE_ID = 2

GENDER_FEMALE = "Female"
GENDER_MALE = "Male"
GENDER_UNKNOWN = "Unknown"

def gender_to_str(gender_id: int) -> str:
    if gender_id == GENDER_FEMALE_ID:
        return GENDER_FEMALE
    elif gender_id == GENDER_MALE_ID:
        return GENDER_MALE
    else:
        return GENDER_UNKNOWN

@strawberry.type
class Query:
    @strawberry.field
    def movies(self, info: Info, title: Optional[str] = None, id: Optional[int] = None, order_by: Optional[str] = None, descending: bool = False, offset: int = 0, limit: int = 100) -> List["Movie"]:
        session: Session = info.context["db"]
        movies_query = select(sql_types.Movie)

        if not title is None:
            movies_query = movies_query.where(sql_types.Movie.title == title)
        if not id is None:
            movies_query = movies_query.where(sql_types.Movie.id == id)
        if not order_by is None:
            sort_fields = {
                "budget": sql_types.Movie.budget,
                "id": sql_types.Movie.id,
                "originalTitle": sql_types.Movie.original_title,
                "title": sql_types.Movie.title,
                "popularity": sql_types.Movie.popularity,
                "revenue": sql_types.Movie.revenue,
                "runtime": sql_types.Movie.runtime,
                "voteAverage": sql_types.Movie.vote_average,
                "voteCount": sql_types.Movie.vote_count,
            }
            sort_field = sort_fields.get(order_by)
            if sort_field is None:
                raise ValueError(f"Field {order_by} not acceptable to sort")
            
            if descending:
                sort_field = sort_field.desc()
            
            movies_query = movies_query.order_by(sort_field)

        movies_query = movies_query.offset(offset).limit(limit)

        return [Movie.from_sql_entity(mov) for mov in session.execute(movies_query).scalars()]
    
    @strawberry.field
    def genres(self, info: Info, name: Optional[str] = None, id: Optional[int] = None) -> List["Genre"]:
        session: Session = info.context["db"]
        genres_query = select(sql_types.Genre)
        
        if not name is None:
            genres_query = genres_query.where(sql_types.Genre.name == name)
        if not id is None:
            genres_query = genres_query.where(sql_types.Genre.id == id)
        
        return [Genre.from_sql_entity(gen) for gen in session.execute(genres_query).scalars()]
    
    @strawberry.field
    def keywords(self, info: Info, name: Optional[str] = None, id: Optional[int] = None, offset: int = 0, limit: int = 100) -> List["Keyword"]:
        session: Session = info.context["db"]
        kw_query = select(sql_types.Keyword)
        
        if not name is None:
            kw_query = kw_query.where(sql_types.Keyword.name == name)
        if not id is None:
            kw_query = kw_query.where(sql_types.Keyword.id == id)
        
        kw_query = kw_query.offset(offset).limit(limit)
        
        return [Keyword.from_sql_entity(kw) for kw in session.execute(kw_query).scalars()]
    
    @strawberry.field
    def production_companies(self, info: Info, name: Optional[str] = None, id: Optional[int] = None, offset: int = 0, limit: int = 100) -> List["ProductionCompany"]:
        session: Session = info.context["db"]
        company_query = select(sql_types.ProductionCompany)
        
        if not name is None:
            company_query = company_query.where(sql_types.ProductionCompany.name == name)
        if not id is None:
            company_query = company_query.where(sql_types.ProductionCompany.id == id)
        
        company_query = company_query.offset(offset).limit(limit)
        
        return [ProductionCompany.from_sql_entity(company) for company in session.execute(company_query).scalars()]
    
    @strawberry.field
    def production_countries(self, info: Info, name: Optional[str] = None, id: Optional[str] = None, offset: int = 0, limit: int = 100) -> List["ProductionCountry"]:
        session: Session = info.context["db"]
        country_query = select(sql_types.ProductionCountry)
        
        if not name is None:
            country_query = country_query.where(sql_types.ProductionCountry.name == name)
        if not id is None:
            country_query = country_query.where(sql_types.ProductionCountry.iso_3166_1 == id)
        
        country_query = country_query.offset(offset).limit(limit)
        
        return [ProductionCountry.from_sql_entity(country) for country in session.execute(country_query).scalars()]
    
    @strawberry.field
    def spoken_languages(self, info: Info, name: Optional[str] = None, id: Optional[str] = None) -> List["SpokenLanguage"]:
        session: Session = info.context["db"]
        lang_query = select(sql_types.SpokenLanguage)
        
        if not name is None:
            lang_query = lang_query.where(sql_types.SpokenLanguage.name == name)
        if not id is None:
            lang_query = lang_query.where(sql_types.SpokenLanguage.iso_639_1 == id)
        
        return [SpokenLanguage.from_sql_entity(lang) for lang in session.execute(lang_query).scalars()]
    
    @strawberry.field
    def cast(self, info: Info, character: Optional[str] = None, id: Optional[str] = None, actor: Optional[str] = None, offset: int = 0, limit: int = 100) -> List["Credit"]:
        session: Session = info.context["db"]
        credit_query = select(sql_types.Credit)
        
        if not character is None:
            credit_query = credit_query.where(sql_types.Credit.character == character)
        if not id is None:
            credit_query = credit_query.where(sql_types.Credit.credit_id == id)
        if not actor is None:
            credit_query = credit_query.where(sql_types.Credit.actor.has(sql_types.Actor.name == actor))
        
        credit_query = credit_query.offset(offset).limit(limit)
        
        return [Credit.from_sql_entity(cred) for cred in session.execute(credit_query).scalars()]
    
    @strawberry.field
    def actor(self, info: Info, name: Optional[str] = None, id: Optional[int] = None, gender: Optional[str] = None, offset: int = 0, limit: int = 100) -> List["Actor"]:
        session: Session = info.context["db"]
        actor_query = select(sql_types.Actor)
        
        if not name is None:
            actor_query = actor_query.where(sql_types.Actor.name == name)
        if not id is None:
            actor_query = actor_query.where(sql_types.Actor.id == id)
        if not gender is None:
            if gender == GENDER_MALE:
                actor_query = actor_query.where(sql_types.Actor.gender == GENDER_MALE_ID)
            elif gender == GENDER_FEMALE:
                actor_query = actor_query.where(sql_types.Actor.gender == GENDER_FEMALE_ID)
            elif gender == GENDER_UNKNOWN:
                actor_query = actor_query.where(sql_types.Actor.gender != GENDER_MALE_ID).where(sql_types.Actor.gender != GENDER_FEMALE_ID)
            else:
                return [] # What do you want else?
        
        actor_query = actor_query.offset(offset).limit(limit)
        
        return [Actor.from_sql_entity(actor) for actor in session.execute(actor_query).scalars()]
    
    @strawberry.field
    def crew(self, info: Info, department: Optional[str] = None, job: Optional[str] = None, id: Optional[str] = None, person: Optional[str] = None, offset: int = 0, limit: int = 100) -> List["CrewCredit"]:
        session: Session = info.context["db"]
        crew_query = select(sql_types.CrewCredit)
        
        if not department is None:
            crew_query = crew_query.where(sql_types.CrewCredit.department == department)
        if not job is None:
            crew_query = crew_query.where(sql_types.CrewCredit.job == job)
        if not id is None:
            crew_query = crew_query.where(sql_types.CrewCredit.credit_id == id)
        if not person is None:
            crew_query = crew_query.where(sql_types.CrewCredit.person.has(sql_types.CrewPerson.name == person))
        
        crew_query = crew_query.offset(offset).limit(limit)
        
        return [CrewCredit.from_sql_entity(cred) for cred in session.execute(crew_query).scalars()]
    
    @strawberry.field
    def crew_person(self, info: Info, id: Optional[int] = None, name: Optional[str] = None, gender: Optional[str] = None, offset: int = 0, limit: int = 100) -> List["CrewPerson"]:
        session: Session = info.context["db"]
        person_query = select(sql_types.CrewPerson)
        
        if not id is None:
            person_query = person_query.where(sql_types.CrewPerson.id == id)
        if not name is None:
            person_query = person_query.where(sql_types.CrewPerson.name == name)
        if not gender is None:
            if gender == GENDER_MALE:
                person_query = person_query.where(sql_types.CrewPerson.gender == GENDER_MALE_ID)
            elif gender == GENDER_FEMALE:
                person_query = person_query.where(sql_types.CrewPerson.gender == GENDER_FEMALE_ID)
            elif gender == GENDER_UNKNOWN:
                person_query = person_query.where(sql_types.CrewPerson.gender != GENDER_MALE_ID).where(sql_types.CrewPerson.gender != GENDER_FEMALE_ID)
            else:
                return [] # Really, why would you like to query something else?
        
        person_query = person_query.offset(offset).limit(limit)
        
        return [CrewPerson.from_sql_entity(person) for person in session.execute(person_query).scalars()]

@strawberry.type
class Movie:
    budget: int
    homepage: str
    id: int
    original_language: str
    original_title: str
    overview: str
    popularity: float
    release_date: str
    revenue: int
    runtime: int
    status: str
    tagline: str
    title: str
    vote_average: float
    vote_count: int

    instance: strawberry.Private[sql_types.Movie]
    
    @strawberry.field
    def genres(self) -> List["Genre"]:
        return [Genre.from_sql_entity(gen) for gen in self.instance.genres]
    
    @strawberry.field
    def keywords(self) -> List["Keyword"]:
        return [Keyword.from_sql_entity(kw) for kw in self.instance.keywords]
    
    @strawberry.field
    def production_companies(self) -> List["ProductionCompany"]:
        return [ProductionCompany.from_sql_entity(company) for company in self.instance.production_companies]
    
    @strawberry.field
    def production_countries(self) -> List["ProductionCountry"]:
        return [ProductionCountry.from_sql_entity(country) for country in self.instance.production_countries]
    
    @strawberry.field
    def spoken_languages(self) -> List["SpokenLanguage"]:
        return [SpokenLanguage.from_sql_entity(lang) for lang in self.instance.spoken_languages]
    
    @strawberry.field
    def cast(self) -> List["Credit"]:
        return [Credit.from_sql_entity(cred) for cred in self.instance.cast]
    
    @strawberry.field
    def crew(self) -> List["CrewCredit"]:
        return [CrewCredit.from_sql_entity(cred) for cred in self.instance.crew]
    
    @classmethod
    def from_sql_entity(cls, movie: sql_types.Movie) -> "Movie":
        return cls(
            budget = movie.budget,
            homepage = movie.homepage,
            id = movie.id,
            original_language = movie.original_language,
            original_title = movie.original_title,
            overview = movie.overview,
            popularity = movie.popularity,
            release_date = movie.release_date,
            revenue = movie.revenue,
            runtime = movie.runtime,
            status = movie.status,
            tagline = movie.tagline,
            title = movie.title,
            vote_average = movie.vote_average,
            vote_count = movie.vote_count,
            instance = movie
        )

@strawberry.type
class Genre:
    id: int
    name: str

    @strawberry.field
    def movies(self, info: Info, offset: int = 0, limit: int = 100) -> List[Movie]:
        session: Session = info.context["db"]
        movies_query = select(sql_types.Movie).where(sql_types.Movie.genres.any(sql_types.Genre.id == self.id)).offset(offset).limit(limit)
        return [Movie.from_sql_entity(mov) for mov in session.execute(movies_query).scalars()]

    @classmethod
    def from_sql_entity(cls, genre: sql_types.Genre) -> "Genre":
        return cls(
            id = genre.id,
            name = genre.name
        )

@strawberry.type
class Keyword:
    id: int
    name: str

    @strawberry.field
    def movies(self, info: Info, offset: int = 0, limit: int = 100) -> List[Movie]:
        session: Session = info.context["db"]
        movies_query = select(sql_types.Movie).where(sql_types.Movie.keywords.any(sql_types.Keyword.id == self.id)).offset(offset).limit(limit)
        return [Movie.from_sql_entity(mov) for mov in session.execute(movies_query).scalars()]
    
    @classmethod
    def from_sql_entity(cls, keyword: sql_types.Keyword) -> "Keyword":
        return cls(
            id = keyword.id,
            name = keyword.name
        )

@strawberry.type
class ProductionCompany:
    id: int
    name: str

    @strawberry.field
    def movies(self, info: Info, offset: int = 0, limit: int = 100) -> List[Movie]:
        session: Session = info.context["db"]
        movies_query = select(sql_types.Movie).where(sql_types.Movie.production_companies.any(sql_types.ProductionCompany.id == self.id)).offset(offset).limit(limit)
        return [Movie.from_sql_entity(mov) for mov in session.execute(movies_query).scalars()]
    
    @classmethod
    def from_sql_entity(cls, company: sql_types.ProductionCompany) -> "ProductionCompany":
        return cls(
            id = company.id,
            name = company.name
        )

@strawberry.type
class ProductionCountry:
    iso_3166_1: str
    name: str

    @strawberry.field
    def movies(self, info: Info, offset: int = 0, limit: int = 100) -> List[Movie]:
        session: Session = info.context["db"]
        movies_query = select(sql_types.Movie).where(sql_types.Movie.production_countries.any(sql_types.ProductionCountry.iso_3166_1 == self.iso_3166_1)).offset(offset).limit(limit)
        return [Movie.from_sql_entity(mov) for mov in session.execute(movies_query).scalars()]
    
    @classmethod
    def from_sql_entity(cls, country: sql_types.ProductionCountry) -> "ProductionCountry":
        return cls(
            iso_3166_1 = country.iso_3166_1,
            name = country.name
        )


@strawberry.type
class SpokenLanguage:
    iso_639_1: str
    name: str

    @strawberry.field
    def movies(self, info: Info, offset: int = 0, limit: int = 100) -> List[Movie]:
        session: Session = info.context["db"]
        movies_query = select(sql_types.Movie).where(sql_types.Movie.spoken_languages.any(sql_types.SpokenLanguage.iso_639_1 == self.iso_639_1)).offset(offset).limit(limit)
        return [Movie.from_sql_entity(mov) for mov in session.execute(movies_query).scalars()]
    
    @classmethod
    def from_sql_entity(cls, lang: sql_types.SpokenLanguage) -> "SpokenLanguage":
        return cls(
            iso_639_1 = lang.iso_639_1,
            name = lang.name
        )

@strawberry.type
class Credit:
    movie_id: strawberry.Private[int]
    actor_id: strawberry.Private[int]
    credit_id: str
    cast_id: int
    character: str
    order: int

    @strawberry.field
    def actor(self, info: Info) -> "Actor":
        session: Session = info.context["db"]
        actor = session.get(sql_types.Actor, self.actor_id)
        return Actor.from_sql_entity(actor)
    
    @strawberry.field
    def movie(self, info: Info) -> Movie:
        session: Session = info.context["db"]
        movie = session.get(sql_types.Movie, self.movie_id)
        return Movie.from_sql_entity(movie)
    
    @classmethod
    def from_sql_entity(cls, credit: sql_types.Credit) -> "Credit":
        return cls(
            movie_id = credit.movie_id,
            actor_id = credit.actor_id,
            credit_id = credit.credit_id,
            cast_id = credit.cast_id,
            character = credit.character,
            order = credit.order
        )

@strawberry.type
class Actor:
    id: int
    gender: str
    name: str

    @strawberry.field
    def cast(self, info: Info, offset: int = 0, limit: int = 100) -> List[Credit]:
        session: Session = info.context["db"]
        cred_query = select(sql_types.Credit).where(sql_types.Credit.actor_id == self.id).offset(offset).limit(limit)
        return [Credit.from_sql_entity(cred) for cred in session.execute(cred_query).scalars()]
    
    @classmethod
    def from_sql_entity(cls, actor: sql_types.Actor) -> "Actor":
        return cls(
            id = actor.id,
            gender = gender_to_str(actor.gender),
            name = actor.name
        )

@strawberry.type
class CrewCredit:
    movie_id: strawberry.Private[int]
    person_id: strawberry.Private[int]
    department: str
    credit_id: str
    job: str

    @strawberry.field
    def person(self, info: Info) -> "CrewPerson":
        session: Session = info.context["db"]
        person = session.get(sql_types.CrewPerson, self.person_id)
        return CrewPerson.from_sql_entity(person)

    @strawberry.field
    def movie(self, info: Info) -> "Movie":
        session: Session = info.context["db"]
        movie = session.get(sql_types.Movie, self.movie_id)
        return Movie.from_sql_entity(movie)
    
    @classmethod
    def from_sql_entity(cls, cred: sql_types.CrewCredit) -> "CrewCredit":
        return cls(
            movie_id = cred.movie_id,
            person_id = cred.person_id,
            department = cred.department,
            credit_id = cred.credit_id,
            job = cred.job
        )

@strawberry.type
class CrewPerson:
    id: int
    gender: str
    name: str
    instance: strawberry.Private[sql_types.CrewPerson]

    @strawberry.field
    def crew(self, info: Info, offset: int = 0, limit: int = 100) -> List[CrewCredit]:
        session: Session = info.context["db"]
        cred_query = select(sql_types.CrewCredit).where(sql_types.CrewCredit.person_id == self.id).offset(offset).limit(limit)
        return [CrewCredit.from_sql_entity(cred) for cred in session.execute(cred_query).scalars()]
    
    @classmethod
    def from_sql_entity(cls, person: sql_types.CrewPerson) -> "CrewPerson":
        return cls(
            id = person.id,
            gender = gender_to_str(person.gender),
            name = person.name,
            instance = person
        )