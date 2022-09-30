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

def get_airport(ident1, ident2):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident ='{ident1}' and ident ='{ident2}';"
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
#get1 = get_airport(tunnus1)
#print(get1[0])
tunnus2 = input("Anna 2. ICAO: ")
get = get_airport(tunnus1,tunnus2)
print(get)

print(f"Etäisyys {tunnus1} - {tunnus2} on {geodesic(get).m:.2f} metria") # metreissa
print(f"Etäisyys {tunnus1} - {tunnus2} on {geodesic(get).km:.2f} kilsaa") # kilsaa