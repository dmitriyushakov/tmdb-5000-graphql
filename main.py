import strawberry
from strawberry.extensions import SchemaExtension
from strawberry.types import ExecutionContext
from sqlalchemy.orm import Session
from strawberry.asgi import GraphQL
from gql_types import Query
from dataset_loader import open_db
from sqlalchemy import Engine
from typing import Optional
import logging

engine_instance: Optional[Engine] = None

def get_engine_instance():
    global engine_instance
    if engine_instance is None:
        engine_instance = open_db()
    return engine_instance

class SQLAlchemySessionExtension(SchemaExtension):
    def __init__(self, *, execution_context: ExecutionContext) -> None:
        self.execution_context = execution_context
        self.engine = get_engine_instance()

    def on_request_start(self):
        self.execution_context.context["db"] = Session(self.engine)

    def on_request_end(self):
        self.execution_context.context["db"].close()

schema = strawberry.Schema(Query, extensions = [SQLAlchemySessionExtension])
app = GraphQL(schema)

if __name__ == '__main__':
    FORMAT = '%(asctime)s - %(message)s'
    logging.basicConfig(format = FORMAT, level = logging.INFO)
    get_engine_instance()
    import uvicorn
    uvicorn.run(app)