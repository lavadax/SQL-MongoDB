import os
import pymysql

# Get username from Gitpod workspace

# username = os.getenv("GITPOD_GIT_USER_NAME")

# Connect to the database
connection = pymysql.connect(host="localhost",
                            user="root",
                            password="",
                            db="Chinook")

try:
    # Run a query
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()