# PYTHON CONNECT TO MSSQL

import pyodbc, pandas

try:
    conn = pyodbc.connect(
        "DRIVER={SQL Server};" "SERVER=localhost\\SQLEXPRESS;" "DATABASE=AdventureWorks2019;" "UID=;" "PWD=;"
    )

    sql = """
    select top 5 JobTitle, OrganizationLevel from HumanResources.Employee
    """
    data = pandas.read_sql_query(sql, conn)

    conn.close()

    print(type(data))
    print(pandas.DataFrame.head(data))

except:
    print("Failed to connect database or execute query")