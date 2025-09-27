# Flask REST API – User Management

## 📌 Objective

A simple REST API built with **Flask** to manage user data using CRUD operations.

---

## 🛠️ Tools

* Python
* Flask
* Postman or Curl

---

## 🚀 Features (Deliverables)

* **GET** → Retrieve all users
* **POST** → Create a new user
* **PUT** → Update an existing user
* **DELETE** → Delete a user

---

## 📂 Project Structure

```
rest_api_flask/
│── app.py
│── README.md
```

---

## 📝 Code Example (app.py)

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

users = {}

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users), 200

@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    user_id = str(len(users) + 1)
    users[user_id] = {"name": data.get("name"), "email": data.get("email")}
    return jsonify({"id": user_id, "message": "User created successfully"}), 201

@app.route("/users/<user_id>", methods=["PUT"])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    data = request.get_json()
    users[user_id]["name"] = data.get("name", users[user_id]["name"])
    users[user_id]["email"] = data.get("email", users[user_id]["email"])
    return jsonify({"message": "User updated successfully"}), 200

@app.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    del users[user_id]
    return jsonify({"message": "User deleted successfully"}), 200

if __name__ == "__main__":
    app.run(debug=True)
```

---

## ▶️ How to Run

1. Clone the repo or download the project.
2. Install Flask:

   ```bash
   pip install flask
   ```
3. Run the app:

   ```bash
   python app.py
   ```
4. The API runs at: `http://127.0.0.1:5000/users`

---

## 🧪 Example Usage with Curl

* **GET all users**

  ```bash
  curl http://127.0.0.1:5000/users
  ```
* **POST create new user**

  ```bash
  curl -X POST http://127.0.0.1:5000/users \
  -H "Content-Type: application/json" \
  -d '{"name": "Alice", "email": "alice@example.com"}'
  ```
* **PUT update user**

  ```bash
  curl -X PUT http://127.0.0.1:5000/users/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "Alice Smith"}'
  ```
* **DELETE remove user**

  ```bash
  curl -X DELETE http://127.0.0.1:5000/users/1
  ```

---

## ✅ Outcome

This project demonstrates **API development fundamentals** by building CRUD routes, handling requests/responses, and testing with Postman or Curl.
