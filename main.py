import json
from flask import Flask, jsonify, abort

app = Flask(__name__)


@app.get("/")
def root():
    f = open('mock-array-data.json', "r")
    all_data = json.load(f)
    return jsonify(all_data)

@app.route("/api/v1/user_count", methods=['GET'])
def count_users():
    data = open("mock-array-data.json", "r")
    all_users = json.load(data)
    user_count = 0
    for user in all_users:
        user_count += 1
    return jsonify({'total registered users': user_count})

@app.route("/api/v1/user_count/<string:requested_data>", methods=['GET'])
def count_requested_data(requested_data):
    data = json.load(open("mock-array-data.json", "r"))
    if requested_data == "email":
        users_with_email = 0
        users = [user for user in data if user['email']]
        for user in users:
            users_with_email += 1
        return jsonify({'users with registered email': users_with_email})
    elif requested_data == "city":
        users_with_city = 0
        users = [user for user in data if user['city']]
        for user in users:
            users_with_city += 1
        return jsonify({'users with associated city': users_with_city})
    else:
        return jsonify({'ERROR': 'bad request'})

@app.route("/api/v1/total_balance", methods=['GET'])
def get_total_balance():
    data = json.load(open("mock-array-data.json"))
    bank_balance = 0
    users = [user for user in data]
    for user in data:
        bank_balance += float(user['account_balance'].strip("$").strip("."))
    return jsonify({'bank balance sheet': f'{bank_balance:,}'})

@app.route('/api/v1/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    data = open('mock-array-data.json', 'r')
    users = json.load(data)
    users = [user for user in users if user['id'] == user_id]
    if len(users) == 0:
        abort(404)
    return jsonify({'user': users[0]})

if __name__ == "__main__":
    app.run(debug=True)