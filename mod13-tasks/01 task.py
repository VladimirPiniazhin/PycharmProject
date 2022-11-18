import json

from flask import Flask, request, Response

app = Flask(__name__)
@app.route("/alkuluku/<number>")
def isPrime(number):
    #args = request.args
    try:
        number = float(number)
        k = 0
        for i in range(2, number // 2 + 1):
            if number % i == 0:
                k += 1
        if k == 0:
            response_dict = {"number": number, "isPrime": "true"}
        else:
            response_dict = {"number": number, "isPrime": "false"}



        response_json = json.dumps(response_dict)

        return Response(response=response_json, status=200, mimetype="application/json")

    except TypeError:
        response_json =json.dumps({"message": "invalid parametrs: missing?", "status": "400 Bad request"})
        return Response(response=response_json, status=400, mimetype="application/json",)

    except ValueError:
        response_json =json.dumps("invalid parametr value: not a number?")
        return Response(response=response_json, status=400, mimetype="application/json")

@app.errorhandler(404)

def page_not_found(error):
    # convert error object (error) to string
    error_text = str(error)
    response_json = json.dumps( {"error": error_text})
    return Response(response=response_json, status=400, mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)