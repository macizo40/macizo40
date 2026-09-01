from flask import Flask, request, jsonify
import secrets
import time

app = Flask(__name__)

# Demo users
USERS = {
    "admin": "SecurePassword123"
}

# In-memory token store
TOKENS = {}

TOKEN_EXPIRATION_SECONDS = 3600


def create_token(username):
    token = secrets.token_urlsafe(32)

    TOKENS[token] = {
        "username": username,
        "created": time.time()
    }

    return token


def validate_token(token):
    token_info = TOKENS.get(token)

    if not token_info:
        return None

    age = time.time() - token_info["created"]

    if age > TOKEN_EXPIRATION_SECONDS:
        del TOKENS[token]
        return None

    return token_info


@app.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if USERS.get(username) != password:
        return jsonify({
            "error": "Invalid credentials"
        }), 401

    token = create_token(username)

    return jsonify({
        "access_token": token,
        "token_type": "Bearer",
        "expires_in": TOKEN_EXPIRATION_SECONDS
    })


@app.route("/data", methods=["POST"])
def exchange_data():

    authorization = request.headers.get(
        "Authorization"
    )

    if not authorization:
        return jsonify({
            "error": "Authorization header missing"
        }), 401

    try:
        token_type, token = authorization.split(" ", 1)

    except ValueError:
        return jsonify({
            "error": "Invalid authorization header"
        }), 401

    if token_type.lower() != "bearer":
        return jsonify({
            "error": "Bearer token required"
        }), 401

    token_info = validate_token(token)

    if not token_info:
        return jsonify({
            "error": "Invalid or expired token"
        }), 401

    data = request.get_json()

    print(
        f"Received secure data from "
        f"{token_info['username']}"
    )

    return jsonify({
        "status": "success",
        "received": data
    })


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )