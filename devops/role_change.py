import json
import sys
from pathlib import Path


ROLE_CHANGE_EVENTS = {
    # Role lifecycle
    "CreateRole",
    "DeleteRole",
    "UpdateRole",
    "UpdateRoleDescription",

    # Trust relationship changes
    "UpdateAssumeRolePolicy",

    # Managed policies attached to roles
    "AttachRolePolicy",
    "DetachRolePolicy",

    # Inline role policies
    "PutRolePolicy",
    "DeleteRolePolicy",

    # Permissions boundary
    "PutRolePermissionsBoundary",
    "DeleteRolePermissionsBoundary",

    # Instance profiles
    "AddRoleToInstanceProfile",
    "RemoveRoleFromInstanceProfile",

    # Tags
    "TagRole",
    "UntagRole",
}


def load_cloudtrail_log(filename):
    """Load a CloudTrail JSON file."""

    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)

    # Standard CloudTrail files contain {"Records": [...]}
    if isinstance(data, dict) and "Records" in data:
        return data["Records"]

    # Also support a JSON array of events
    if isinstance(data, list):
        return data

    raise ValueError("Unsupported CloudTrail JSON format")


def get_role_name(event):
    """Try to identify the AWS IAM role affected."""

    params = event.get("requestParameters") or {}

    return (
        params.get("roleName")
        or params.get("role")
        or "Unknown"
    )


def filter_role_changes(events):
    """Return only events that modify IAM roles."""

    results = []

    for event in events:

        event_name = event.get("eventName")

        if event_name not in ROLE_CHANGE_EVENTS:
            continue

        user_identity = event.get("userIdentity") or {}

        results.append({
            "eventTime": event.get("eventTime"),
            "eventName": event_name,
            "roleName": get_role_name(event),
            "performedBy": (
                user_identity.get("arn")
                or user_identity.get("principalId")
                or "Unknown"
            ),
            "sourceIPAddress": event.get("sourceIPAddress"),
            "awsRegion": event.get("awsRegion"),
            "eventID": event.get("eventID"),
        })

    return results


def print_events(events):

    if not events:
        print("No AWS role changes found.")
        return

    print(f"\nAWS ROLE CHANGES FOUND: {len(events)}")
    print("=" * 90)

    for event in events:
        print(f"Time       : {event['eventTime']}")
        print(f"Action     : {event['eventName']}")
        print(f"Role       : {event['roleName']}")
        print(f"PerformedBy: {event['performedBy']}")
        print(f"Source IP  : {event['sourceIPAddress']}")
        print(f"Region     : {event['awsRegion']}")
        print(f"Event ID   : {event['eventID']}")
        print("-" * 90)


def save_results(events, output_file):

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(events, file, indent=4)

    print(f"\nFiltered events saved to: {output_file}")


def main():

    if len(sys.argv) < 2:
        print("Usage:")
        print("python aws_role_changes.py cloudtrail.json")
        sys.exit(1)

    input_file = Path(sys.argv[1])

    if not input_file.exists():
        print(f"File not found: {input_file}")
        sys.exit(1)

    try:
        events = load_cloudtrail_log(input_file)

        role_changes = filter_role_changes(events)

        print_events(role_changes)

        save_results(
            role_changes,
            "aws_role_changes.json"
        )

    except Exception as error:
        print(f"Error processing log: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()