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


def get_country(iso_code):
    #sql = "SELECT * FROM country where iso_country = 'FI';"
    sql = "SELECT rownum(), iso_country, name, wikipedia_link FROM country;"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall() #type of result: list
    #print("Koko tuloslista: ", result)
    #print("Tuloksia yhteensä: ", cursor.rowcount)
    if cursor.rowcount > 0:
        for row in result:
            print(f"{row[0]}: {row[1]}, {row[2]} wikipedia: {row[3]}")
    else:
        print("Ei ole tuloksia")

get_country('FI')

print()