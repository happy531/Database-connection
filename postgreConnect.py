# PYTHON CONNECT TO POSTGRESQL

import psycopg2, pandas

try:
    conn = psycopg2.connect(host="", dbname="", user="", password="")

    sql = """
    select * from Table
    """
    data = pandas.read_sql_query(sql, conn)

    conn.close()

    print(type(data))
    print(pandas.DataFrame.head(data))

except:
    print("Failed to connect database or execute query")