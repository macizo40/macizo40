
from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("http-security")


SECURITY_HEADERS = {
    "X-Content-Type-Options": "nosniff",
    "X-Frame-Options": "DENY",
    "Referrer-Policy": "strict-origin-when-cross-origin",
    "Content-Security-Policy": (
        "default-src 'self'; "
        "script-src 'self'; "
        "style-src 'self'; "
        "img-src 'self' data:; "
        "object-src 'none'; "
        "base-uri 'self'; "
        "frame-ancestors 'none'"
    ),
    "Permissions-Policy": (
        "camera=(), microphone=(), geolocation=()"
    ),
    "Strict-Transport-Security": (
        "max-age=31536000; includeSubDomains"
    ),
    "Cache-Control": "no-store"
}


@app.after_request
def add_security_headers(response):
    """
    Add security headers to every HTTP response.
    """

    for header, value in SECURITY_HEADERS.items():

        # HSTS must only be sent over HTTPS.
        # Behind a reverse proxy, configure ProxyFix
        # and trusted proxy settings correctly.
        if header == "Strict-Transport-Security":
            if not request.is_secure:
                continue

        response.headers[header] = value

    # Remove unnecessary server identification
    response.headers.pop("X-Powered-By", None)

    logger.info(
        "HTTP response: method=%s path=%s status=%s",
        request.method,
        request.path,
        response.status_code
    )

    return response


@app.route("/")
def home():
    return jsonify({
        "status": "success",
        "message": "HTTP security headers enabled"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )
