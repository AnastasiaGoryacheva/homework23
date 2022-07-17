import os

from flask import Flask, request, abort

from utils import construct_query

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route("/perform_query", methods=['GET', 'POST'])
def perform_query():
    try:
        cmd_1 = request.args["cmd_1"]
        value_1 = request.args["value_1"]
        cmd_2 = request.args["cmd_2"]
        value_2 = request.args["value_2"]
        file_name = request.args["file_name"]
    except Exception:
        abort(400, "Incorrect query")
    file_path = os.path.join(DATA_DIR, file_name)
    if not os.path.exists(file_path):
        abort(400, "File not found")

    with open(file_name, encoding='utf-8') as file:
        result = construct_query(cmd_1, value_1, file)
        result = construct_query(cmd_2, value_2, result)
        result = "/n".join(result)

    return app.response_class(result, content_type="text/plain")


if __name__ == '__main__':
    app.run(debug=True)
