# Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit. Ohjelma ilmoittaa
# lentokenttien välisen etäisyyden kilometreinä. Laskenta perustuu tietokannasta haettuihin koordinaatteihin.
# Laske etäisyys geopy-kirjaston avulla: https://geopy.readthedocs.io/en/stable/. Asenna kirjasto valitsemalla
# View / Tool Windows / Python Packages. Kirjoita hakukenttään geopy ja vie asennus loppuun.

from geopy.distance import geodesic
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
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident ='{ident}';"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall() #type of result: list
    return result
    #print("Koko tuloslista: ", result)
    #print("Tuloksia yhteensä: ", cursor.rowcount)
    #if cursor.rowcount > 0:
        #for row in result:
            #print(f"{row[0]}: {row[1]}")
    #else:
        #print("Ei ole tuloksia")

tunnus1 = input("Anna 1. ICAO: ")
get1 = get_airport(tunnus1)
print(get1[0])
tunnus2 = input("Anna 2. ICAO: ")
get2 = get_airport(tunnus2)
print(get2[0])
print(f"Etäisyys {tunnus1} - {tunnus2} on {geodesic(get1[0], get2[0]).m:.2f} metria") # metreissa
print(f"Etäisyys {tunnus1} - {tunnus2} on {geodesic(get1[0], get2[0]).km:.2f} kilsaa") # kilsaa


