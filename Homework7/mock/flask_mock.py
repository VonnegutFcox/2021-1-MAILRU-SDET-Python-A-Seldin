import json
import threading

from flask import Flask, jsonify, request

import settings

app = Flask(__name__)

SURNAME_DATA = {}
ID = 1


@app.route('/create_surname', methods=['POST'])
def create_user_surname(name):
    global ID
    name = json.loads(request.data)['name']
    if name in SURNAME_DATA:
        return jsonify(f'Name {name} is already exists'), 404
    SURNAME_DATA.update({name: ID})
    ID += 1
    return jsonify({'ID': ID}), 201

    # if name not in SURNAME_DATA:
    #     SURNAME_DATA[name] = ID
    #     data = {'ID': ID}
    #     ID += 1
    #     return jsonify(data), 201
    # else:
    #     return jsonify(f'Name {name} is already exists'), 404


@app.route('/get_surname/<name>', methods=['GET'])
def get_user_surname(name):
    if surname := SURNAME_DATA.get(name):
        return jsonify(surname), 200
    else:
        return jsonify(f'Surname for user {name} not fount'), 404


@app.route('/create_surname', methods=['PUT'])
def put_user_surname(name):
    global ID
    name = json.loads(request.data)['name']
    if name in SURNAME_DATA:
        SURNAME_DATA[name] = ID
        return jsonify(f'Name {name} is replaced'), 404
    SURNAME_DATA[name] = ID
    ID += 1
    return jsonify({'ID': ID}), 201


@app.route("/get_surname/<name>", methods=["DELETE"])
def delete_user(name):
    if name in SURNAME_DATA:
        del SURNAME_DATA[name]
        return jsonify({}), 204
    return jsonify(f'Surname for user {name} not fount'), 404


def run_mock():
    server = threading.Thread(target=app.run, kwargs={
        'host': settings.MOCK_HOST,
        'port': settings.MOCK_PORT
    })
    server.start()
    return server


def shutdown_mock():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()


@app.route('/shutdown')
def shutdown():
    shutdown_mock()
    return jsonify(f'OK, exiting'), 200