import socket
import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime

HOST = "0.0.0.0"
PORT = 514

LOG_FILE = "syslog_collector.log"

# Configure logging with rotation
logger = logging.getLogger("SyslogCollector")
logger.setLevel(logging.INFO)

handler = RotatingFileHandler(
    LOG_FILE,
    maxBytes=100 * 1024 * 1024,  # 100 MB
    backupCount=10
)

formatter = logging.Formatter(
    "%(asctime)s %(message)s"
)

handler.setFormatter(formatter)
logger.addHandler(handler)


def start_syslog_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Allow reuse of the port
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    sock.bind((HOST, PORT))

    print(f"Syslog collector listening on UDP {HOST}:{PORT}")
    print(f"Writing logs to: {LOG_FILE}")

    while True:
        try:
            data, address = sock.recvfrom(65535)

            message = data.decode("utf-8", errors="replace").strip()

            timestamp = datetime.now().isoformat()

            log_entry = (
                f"{timestamp} "
                f"source={address[0]}:{address[1]} "
                f"{message}"
            )

            logger.info(log_entry)

            print(log_entry)

        except KeyboardInterrupt:
            print("\nStopping syslog collector...")
            break

        except Exception as e:
            print(f"Error receiving syslog: {e}")

    sock.close()


if __name__ == "__main__":
    start_syslog_server()