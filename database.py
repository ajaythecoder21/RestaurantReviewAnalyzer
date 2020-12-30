import psycopg2



cur.execute("CREATE TABLE res (sentiment VARCHAR);")


cur.execute("INSERT INTO res (sentiment) VALUES(%s)", ())

conn.commit()


conn.close()