# Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI) ja tulostaa kyseisessä maassa olevien
# lentokenttien lukumäärät tyypeittäin. Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä, että pieniä
# lentokenttiä on 65 kappaletta, helikopterikenttiä on 15 kappaletta jne.
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

def get_airport(iso_country):
    sql = f"SELECT type, COUNT(type) FROM airport WHERE iso_country ='{iso_country}' group by type;"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall() #type of result: list
    #print("Koko tuloslista: ", result)
    #print("Tuloksia yhteensä: ", cursor.rowcount)
    if cursor.rowcount > 0:
        for row in result:
            print(f"{row[0]}: {row[1]}")
    else:
        print("Ei ole tuloksia")

tunnus = input("Anna maan tunnus: ")
get_airport(tunnus)