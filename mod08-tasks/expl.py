
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

connection = connect_database()
maa = input("Maakoodi: ")

sql = f"SELECT type, COUNT(*) FROM airport WHERE iso_country ='"+ maa +"' group by type;"
cursor = connection.cursor()
cursor.execute(sql)
result = cursor.fetchall() #type of result: list
    #print("Koko tuloslista: ", result)
    #print("Tuloksia yhteensä: ", cursor.rowcount)
for rivi in result
    print(f"{rivi[0]} {rivi[1]}")