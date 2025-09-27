from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory user data storage (dictionary for demo purpose)
users = {}

# -------------------------------
# 1. GET - Retrieve all users
# -------------------------------
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users), 200


# -------------------------------
# 2. POST - Add a new user
# -------------------------------
@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    user_id = str(len(users) + 1)  # auto-generate ID
    users[user_id] = {
        "name": data.get("name"),
        "email": data.get("email")
    }
    return jsonify({"id": user_id, "message": "User created successfully"}), 201


# -------------------------------
# 3. PUT - Update a user
# -------------------------------
@app.route("/users/<user_id>", methods=["PUT"])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    
    data = request.get_json()
    users[user_id]["name"] = data.get("name", users[user_id]["name"])
    users[user_id]["email"] = data.get("email", users[user_id]["email"])
    
    return jsonify({"message": "User updated successfully"}), 200


# -------------------------------
# 4. DELETE - Remove a user
# -------------------------------
@app.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    
    del users[user_id]
    return jsonify({"message": "User deleted successfully"}), 200


if __name__ == "__main__":
    app.run(debug=True)
