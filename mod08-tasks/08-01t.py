import mysql.connector
def connect_database():
    return mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='Yahoo',
         autocommit=True
         )