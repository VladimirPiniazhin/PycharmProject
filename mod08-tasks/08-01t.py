#Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin. Ohjelma hakee ja tulostaa koodia vastaavan
# lentokentän nimen ja sen sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta


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

def get_airport(ident):
    sql = f"SELECT name, iso_region FROM airport WHERE ident ='{ident}';"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall() #type of result: list
    print("Koko tuloslista: ", result)
    print("Tuloksia yhteensä: ", cursor.rowcount)


isao = input("Anna ISAO: ")
get_airport(isao)