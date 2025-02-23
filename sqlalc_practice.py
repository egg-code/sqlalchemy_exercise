from sqlalchemy import create_engine, select, text
from sqlalchemy.orm import Session, DeclarativeBase
from models import Books, Author_Details, Base
import pandas as pd


#connect_db & create tables
engine = create_engine("sqlite:///egg.db")
conn = engine.connect()
Base.metadata.create_all(engine) # create tables from models.py

#Insert data into sqlite tables
books_df = pd.read_csv("./books.csv")
author_details_df = pd.read_csv("./author_details.csv")

books_df.to_sql('books', engine, if_exists='replace', index=False)
author_details_df.to_sql('author_details', engine, if_exists='replace', index=False)

## 1. Select book_id, title, author_name from egg.db
query_1 = text("SELECT B.book_id, B.title, A.author_name FROM books B, author_details A WHERE A.author_id = B.author_id;")
result_1 = conn.execute(query_1)
for row in result_1:
    print(row)

## 2. Select author_name and count of books
query_2 = text("SELECT A.author_name, COUNT(B.book_id) as book_count FROM books B JOIN author_details A ON A.author_id = B.author_id GROUP BY A.author_name;")
result_2 = conn.execute(query_2)
for row in result_2:
    print(row)

# Read data from tables using ORM
with Session(engine) as session:
    query_b = select(Books) # select all columns from Books table 
    for book in session.scalars(query_b):
        print(book)
    
    query_a = select(Author_Details) # select all columns from Author_Details table
    for author in session.scalars(query_a):
        print(author)

# Close connection
conn.close()








