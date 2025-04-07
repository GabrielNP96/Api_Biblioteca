from sqlmodel import SQLModel, create_engine
from app.models import Book

#caminho para o banco de dados
sqlite_file_name = "library.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

#criar o "motor" de conexão com o sqlite
engine = create_engine(sqlite_url, echo=True)

#função que cria as tabelas

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)