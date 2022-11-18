import json

from flask import Flask, request, Response

app = Flask(__name__)
@app.route('/summa')
def summa():
    args = request.args

    try:
        luku1 = float(args.get("luku1"))
        luku2 = float(args.get("luku2"))
        summa = luku1+luku2

        response_dict = {
            "luku1": luku1,
            "luku2": luku2,
            "summa": summa
        }

        response_json = json.dumps(response_dict)

        return Response(response=response_json, status=200, mimetype="application/json")

    except TypeError:
        response_json =json.dumps("invalid parametrs: missing?")
        return Response(response=response_json, status=400, mimetype="application/json",)

    except ValueError:
        response_json =json.dumps("invalid parametr value: not a number?")
        return Response(response=response_json, status=400, mimetype="application/jsonmimetype=")






@app.route('/kukkuu')

def do_something():
    return "Moro"

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)