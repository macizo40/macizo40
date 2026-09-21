import csv
from collections import Counter, defaultdict
from datetime import datetime

LOG_FILE = "login_metrics.csv"

# Expected CSV format:
#
# timestamp,user_id,login_method,status
# 2026-09-21 09:10:01,user001,password,success
# 2026-09-21 09:11:22,user002,otp,success
# 2026-09-21 09:12:10,user003,email,failure
# 2026-09-21 09:13:15,user001,password,failure


def read_login_events(filename):
    events = []

    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                event = {
                    "timestamp": datetime.strptime(
                        row["timestamp"],
                        "%Y-%m-%d %H:%M:%S"
                    ),
                    "user_id": row["user_id"],
                    "method": row["login_method"].lower(),
                    "status": row["status"].lower()
                }

                events.append(event)

            except (KeyError, ValueError) as error:
                print(f"Invalid row: {row}")
                print(f"Reason: {error}")

    return events


def calculate_metrics(events):

    supported_methods = {"password", "otp", "email"}

    total_logins = Counter()
    successful_logins = Counter()
    failed_logins = Counter()

    unique_users = defaultdict(set)

    for event in events:

        method = event["method"]

        if method not in supported_methods:
            continue

        total_logins[method] += 1
        unique_users[method].add(event["user_id"])

        if event["status"] == "success":
            successful_logins[method] += 1

        elif event["status"] == "failure":
            failed_logins[method] += 1

    return (
        total_logins,
        successful_logins,
        failed_logins,
        unique_users
    )


def print_metrics(events):

    (
        total,
        success,
        failure,
        users
    ) = calculate_metrics(events)

    print("\nAUTHENTICATION METRICS")
    print("=" * 70)

    print(
        f"{'Method':<12}"
        f"{'Total':<10}"
        f"{'Success':<10}"
        f"{'Failed':<10}"
        f"{'Success %':<12}"
        f"{'Users':<10}"
    )

    print("-" * 70)

    for method in ["password", "otp", "email"]:

        attempts = total[method]
        successful = success[method]
        failed = failure[method]

        success_rate = (
            successful / attempts * 100
            if attempts > 0
            else 0
        )

        print(
            f"{method.upper():<12}"
            f"{attempts:<10}"
            f"{successful:<10}"
            f"{failed:<10}"
            f"{success_rate:<12.2f}"
            f"{len(users[method]):<10}"
        )


def main():

    try:
        events = read_login_events(LOG_FILE)

        print(f"Events processed: {len(events)}")

        print_metrics(events)

    except FileNotFoundError:
        print(f"File not found: {LOG_FILE}")


if __name__ == "__main__":
    main()