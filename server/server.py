from flask import Flask, request
from flask_cors import CORS
from db import get_all, find_same_users, add_new_member, delete_all, string_to_map

app = Flask(__name__)
CORS(app)


@app.route('/get_all_users', methods=["get"])
def get_all_users():
    data = get_all()
    return {
        "data": string_to_map(data),
        "count": len(data)
    }


@app.route('/find_users', methods=["get"])
def find_users():
    data = find_same_users(request.args.get("key"))

    return {
        "data": string_to_map(data),
        "count": len(data)
    }


@app.route('/add_user', methods=["post"])
def add_new_user():
    add_new_member(
        request.args.get("name"),
        request.args.get("email"),
        request.args.get("number"),
        request.args.get("photo"),
        request.args.get("roles"),
        request.args.get("interests"),
        request.args.get("departament")
    )

    return "OK"


@app.route('/delete_all', methods=["post"])
def delete_all_users():
    delete_all()
    return "OK"


if __name__ == '__main__':
    app.run(debug=True, port=5000)
