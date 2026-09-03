import requests
import time
from datetime import datetime

INCODE_URL = "https://your-incode-endpoint.com/health"
TIMEOUT = 10


def check_incode_service():
    print("=" * 55)
    print("Incode Service Availability Check")
    print("=" * 55)

    start_time = time.time()

    try:
        response = requests.get(
            INCODE_URL,
            timeout=TIMEOUT
        )

        latency = (time.time() - start_time) * 1000

        print(f"Time       : {datetime.now()}")
        print(f"Endpoint   : {INCODE_URL}")
        print(f"HTTP Code  : {response.status_code}")
        print(f"Latency    : {latency:.2f} ms")

        if 200 <= response.status_code < 300:
            print("Status     : AVAILABLE")
            return True

        elif 400 <= response.status_code < 500:
            print("Status     : REACHABLE")
            print("Warning    : Authentication or request issue.")
            return True

        elif response.status_code >= 500:
            print("Status     : SERVICE ERROR")
            return False

    except requests.exceptions.Timeout:
        print("Status     : UNAVAILABLE")
        print(f"Reason     : Timeout after {TIMEOUT} seconds")
        return False

    except requests.exceptions.ConnectionError:
        print("Status     : UNAVAILABLE")
        print("Reason     : Connection failed")
        return False

    except requests.exceptions.RequestException as error:
        print("Status     : ERROR")
        print(f"Reason     : {error}")
        return False


if __name__ == "__main__":
    check_incode_service()