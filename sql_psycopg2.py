"""elkjdflkjlksdjflkjsd
"""

import psycopg2


# connect to "chinook" database
connection = psycopg2.connect(
    host = "localhost",
    database = "chinook",
    user = "postgres",
    password = "Arif1234"
)

# build a cursor object of the database
cursor = connection.cursor()

# Query1 - select all records from "Artist" table
# cursor.execute('SELECT * FROM "Artist"')
# cursor.execute('SELECT "Name" FROM "Artist"')
# cursor.execute('SELECT * FROM "Artist" where "Name" = %s', ["Queen"])
# cursor.execute('SELECT * FROM "Album" WHERE "ArtsitId" = %s', [51])
cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# fetch the result (multiple)
results = cursor.fetchall()

# fetch the result single
# results = cursor.fetchone()

connection.close()

# print result
for result in results:
    print(result)
