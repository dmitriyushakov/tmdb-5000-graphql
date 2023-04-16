# TMDB 5000 Movie GraphQL service
It is toy GraphQL service written to play with SQLAlchemy and GraphQL. There used data parsed from ["TMDB 5000 Movie Dataset"](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) dataset published on Kaggle. It allow to query all kind of entities present in this dataset with relationships between them using by GraphQL.


## Start to work

I recommend to start work in virtual python environment.

On Windows:
```
python -m venv env
env\Scripts\activate.bat
```
On Linux:
```
python -m venv env
source env/bin/activate
```

After that install reqierements:
```
pip install -r requirements.txt
```

After that application can be started by running `main.py`. Script automatically will generate SQLite database and fill it by parsing dataset first time. After few minutes GraphQL app will be started with `uvicorn` server. Next time starting will be faster:
```
python main.py
```

After start GraphiQL interface will be available at:

http://127.0.0.1:8000/


## GraphQL schema

See generated GraphQL schema in [generated_schema.gql](generated_schema.gql)


## Examples

See some [examles of queries](QUERY_EXAMPLES.md) to this GraphQL

