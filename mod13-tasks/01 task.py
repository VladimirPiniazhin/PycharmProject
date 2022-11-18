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
        responseText ="invalid parametrs: missing?"
        return Response(response=responseText, status=400)

    except ValueError:
        responseText ="invalid parametr value: not a number?"
        return Response(response=responseText, status=400)






@app.route('/kukkuu')

def do_something():
    return "Moro"

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)