import os

from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

load_dotenv()

postgres_url = os.getenv('POSTGRES_URL')
postgres_engine = create_engine(postgres_url, echo=True)
sqlite_engine = create_engine("sqlite:///egg.db")

books_df = pd.read_sql_table('books', sqlite_engine)
authors_df = pd.read_sql_table('author_details', sqlite_engine)

books_df.to_sql('books', postgres_engine, if_exists='replace', index=False)
authors_df.to_sql('author_details', postgres_engine, if_exists='replace', index=False)
print(f"Successfully added data from SQLite into Postgres!")

sqlite_engine.dispose()
postgres_engine.dispose()