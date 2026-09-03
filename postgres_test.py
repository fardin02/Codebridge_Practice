import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="python_learning",
    user="postgres",
    password="p12345",
    port="5432"
)

print("Database connected successfully!")

connection.close()