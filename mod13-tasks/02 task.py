import json
from flask import Flask, request, Response
import mysql.connector


def connect_database():
    return mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password='Yahoo',
        autocommit=True
    )
connection = connect_database()


def get_airport(isao):
    sql = f"SELECT name, municipality FROM airport WHERE ident ='{isao}';"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()  # type of result: list
    print("Koko tuloslista: ", result)
    print("Tuloksia yhteensä: ", cursor.rowcount)
    return result

app = Flask(__name__)

@app.route("/kentta/<isao>")
def kentta(isao):
    #args = request.args
    try:
        get_list = get_airport(isao)
        response_json = {"ICAO": isao, "Name": get_list[0][0], "Municipality": get_list[0][1]}
        #response_json = json.dumps(response_dict)

        return Response(response=response_json, status=200, mimetype="application/json")

    except TypeError:
        response_json = json.dumps({"message": "invalid parametrs: missing?", "status": "400 Bad request"})
        return Response(response=response_json, status=400, mimetype="application/json",)

    except ValueError:
        response_json = json.dumps("invalid parametr value: not a number?")
        return Response(response=response_json, status=400, mimetype="application/json")

@app.errorhandler(404)
def page_not_found(error):
    #convert error object (error) to string
    error_text = str(error)
    response_json = json.dumps({"error": error_text})
    return Response(response=response_json, status=400, mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)