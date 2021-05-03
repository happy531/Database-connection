# PYTHON CONNECT TO MSSQL

import pyodbc, pandas

try:
    conn = pyodbc.connect("DRIVER={SQL Server};" "SERVER=;" "DATABASE=;" "UID=;" "PWD=;")

    sql = """
    select * from Autorzy
    """
    data = pandas.read_sql_query(sql, conn)

    conn.close()

    print(type(data))
    print(pandas.DataFrame.head(data))

except:
    print("Failed to connect database or execute query")