from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# En producción, cargar desde DB, Redis, ConfigMap, etc.
CANARY_WHITELIST = {
    "user-1001",
    "user-1002",
    "qa-team",
    "devops-team"
}

STABLE_BACKEND = os.getenv(
    "STABLE_BACKEND",
    "http://stable-service:8080"
)

CANARY_BACKEND = os.getenv(
    "CANARY_BACKEND",
    "http://canary-service:8080"
)


def is_canary_user(user_id: str) -> bool:
    """Determina si el usuario debe utilizar la versión canary."""
    if not user_id:
        return False

    return user_id in CANARY_WHITELIST


def select_backend(user_id: str) -> dict:
    """Selecciona stable o canary."""

    if is_canary_user(user_id):
        return {
            "version": "canary",
            "backend": CANARY_BACKEND
        }

    return {
        "version": "stable",
        "backend": STABLE_BACKEND
    }


@app.route("/route", methods=["GET"])
def route_request():

    user_id = request.headers.get("X-User-ID")

    deployment = select_backend(user_id)

    return jsonify({
        "user": user_id,
        "deployment": deployment["version"],
        "backend": deployment["backend"]
    })


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy"
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8080
    )