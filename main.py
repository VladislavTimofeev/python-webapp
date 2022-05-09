from flask import Flask, request, json

app = Flask(__name__)


@app.route('/api/v1/users', methods=['POST'])
def post_method():
    req_body = request.json
    return json.jsonify(req_body)


@app.route('/api/v1/users', methods=['GET'])
def get_method():
    page = request.args.get("page")
    print(page)
    resp = {
        "users": [
            {
                "name": "id1"
            },
            {
                "name": "id2"
            }
        ]
    }
    return resp


@app.route('/api/v1/users/<id>')
def get_user_by_id(id):
    print(id)
    user = {
        "name": "Mike",
        "id": id
    }
    return user


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8000)
