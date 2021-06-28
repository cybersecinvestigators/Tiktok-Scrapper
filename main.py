import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True
f1 = open('list.txt', 'r')
list1 = f1.readlines()


@app.route('/<int:rid>', methods=['GET'])
def fetching(rid):
    response = jsonify({"data": list1[rid].replace('\n', '')})
    response.headers.add("Access-Control-Allow-Origin", "*")
    print(response.data)
    return response


@app.route('/check', methods=['POST'])
def check():
    code = request.data
    print(code)
    response = jsonify({"status": 200})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


if __name__ == '__main__':
    app.run()
