import requests


SERVER = "http://127.0.0.1:5000"


def get_token():

    response = requests.post(
        f"{SERVER}/login",
        json={
            "username": "admin",
            "password": "SecurePassword123"
        },
        timeout=10
    )

    response.raise_for_status()

    return response.json()["access_token"]


def send_information(token):

    information = {
        "system": "AWS",
        "environment": "production",
        "message": "Secure information exchange",
        "server_count": 25
    }

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.post(
        f"{SERVER}/data",
        json=information,
        headers=headers,
        timeout=10
    )

    response.raise_for_status()

    print(response.json())


def main():

    token = get_token()

    print("Authentication successful.")

    send_information(token)


if __name__ == "__main__":
    main()