
import boto3
import sqlite3
import json
import argparse
from datetime import datetime, timedelta, timezone
from botocore.exceptions import BotoCoreError, ClientError

DB_NAME = "aws_events.db"

SECURITY_EVENTS = {
    "ConsoleLogin",
    "CreateUser",
    "DeleteUser",
    "CreateAccessKey",
    "DeleteAccessKey",
    "AttachUserPolicy",
    "DetachUserPolicy",
    "PutUserPolicy",
    "CreateRole",
    "DeleteRole",
    "AssumeRole",
    "AuthorizeSecurityGroupIngress",
    "RevokeSecurityGroupIngress",
    "StopLogging",
    "DeleteTrail",
    "PutBucketPolicy",
    "DeleteBucketPolicy",
    "RunInstances",
    "TerminateInstances"
}


def init_database():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS aws_events (
                event_id TEXT PRIMARY KEY,
                event_time TEXT,
                event_name TEXT,
                event_source TEXT,
                username TEXT,
                aws_region TEXT,
                severity TEXT,
                event_data TEXT
            )
        """)


def classify_event(event_name, event_data):
    if event_name in {
        "StopLogging", "DeleteTrail",
        "DeleteUser", "DeleteAccessKey",
        "DeleteBucketPolicy"
    }:
        return "HIGH"

    if event_name == "ConsoleLogin":
        response = event_data.get("responseElements") or {}
        if response.get("ConsoleLogin") == "Failure":
            return "HIGH"
        return "INFO"

    if event_name in SECURITY_EVENTS:
        return "MEDIUM"

    return "INFO"


def save_event(event, region):
    raw_event = json.loads(event.get("CloudTrailEvent", "{}"))
    event_name = event.get("EventName", "Unknown")
    severity = classify_event(event_name, raw_event)

    record = (
        event["EventId"],
        event["EventTime"].isoformat(),
        event_name,
        event.get("EventSource", ""),
        event.get("Username", ""),
        region,
        severity,
        json.dumps(raw_event, default=str)
    )

    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.execute("""
            INSERT OR IGNORE INTO aws_events
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, record)
        return cursor.rowcount


def collect_events(region, hours, profile=None):
    session = boto3.Session(
        profile_name=profile,
        region_name=region
    )

    client = session.client("cloudtrail")

    end_time = datetime.now(timezone.utc)
    start_time = end_time - timedelta(hours=hours)

    paginator = client.get_paginator("lookup_events")

    total = 0

    try:
        for page in paginator.paginate(
            StartTime=start_time,
            EndTime=end_time
        ):
            for event in page.get("Events", []):
                total += save_event(event, region)

        print(f"Region: {region}")
        print(f"New events saved: {total}")
        print(f"Database: {DB_NAME}")

    except (ClientError, BotoCoreError) as error:
        print(f"AWS error: {error}")
        raise


def show_events(limit=20):
    with sqlite3.connect(DB_NAME) as conn:
        rows = conn.execute("""
            SELECT event_time, event_name,
                   username, aws_region, severity
            FROM aws_events
            ORDER BY event_time DESC
            LIMIT ?
        """, (limit,)).fetchall()

    for row in rows:
        print(" | ".join(str(value) for value in row))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="AWS CloudTrail Event Collector"
    )

    parser.add_argument("--region", default="us-east-1")
    parser.add_argument("--hours", type=int, default=24)
    parser.add_argument("--profile", default=None)
    parser.add_argument("--show", action="store_true")

    args = parser.parse_args()

    init_database()

    if args.show:
        show_events()
    else:
        collect_events(
            region=args.region,
            hours=args.hours,
            profile=args.profile
        )
