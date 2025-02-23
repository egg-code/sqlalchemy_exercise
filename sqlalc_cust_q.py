from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///egg.db")
def custom_q(q_stmt: str):
    stmt = text(q_stmt)
    with engine.connect() as conn:
        data = conn.execute(stmt)
        return data

input_query = input("Enter your query: ")
output = custom_q(input_query)

# Check if the query contains COUNT
if 'count' in input_query.lower():
    print(f"Total count: {output.fetchone()[0]}")
else:
    for row in output:
        print(row)