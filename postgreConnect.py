# PYTHON CONNECT TO POSTGRESQL

import psycopg2, pandas

try:
    conn = psycopg2.connect(dbname="", user="", password="", host="")

    sql = """
    select * from Autorzy
    """
    data = pandas.read_sql_query(sql, conn)

    conn.close()

    print(type(data))
    print(pandas.DataFrame.head(data))

except:
    print("Failed to connect database")