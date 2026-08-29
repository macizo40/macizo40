import boto3
from botocore.exceptions import ClientError

# AWS managed policy
READ_ONLY_POLICY_ARN = "arn:aws:iam::aws:policy/ReadOnlyAccess"

GROUP_NAME = "ReadOnlyUsers"


def get_iam_client():
    return boto3.client("iam")


def create_group_if_needed(iam):
    try:
        iam.get_group(GroupName=GROUP_NAME)
        print(f"Group '{GROUP_NAME}' already exists.")

    except iam.exceptions.NoSuchEntityException:
        iam.create_group(GroupName=GROUP_NAME)
        print(f"Created IAM group: {GROUP_NAME}")


def attach_readonly_policy(iam):
    iam.attach_group_policy(
        GroupName=GROUP_NAME,
        PolicyArn=READ_ONLY_POLICY_ARN
    )

    print(f"Attached ReadOnlyAccess policy to {GROUP_NAME}.")


def get_all_users(iam):
    users = []

    paginator = iam.get_paginator("list_users")

    for page in paginator.paginate():
        users.extend(page["Users"])

    return users


def add_user_to_group(iam, username):
    try:
        iam.add_user_to_group(
            GroupName=GROUP_NAME,
            UserName=username
        )

        print(f"Added {username} to {GROUP_NAME}")

    except ClientError as error:
        print(
            f"Failed to add {username}: "
            f"{error.response['Error']['Message']}"
        )


def assign_readonly_to_all_users():

    iam = get_iam_client()

    print("Creating/configuring ReadOnly group...")

    create_group_if_needed(iam)

    attach_readonly_policy(iam)

    print("\nGetting IAM users...")

    users = get_all_users(iam)

    print(f"Found {len(users)} IAM users.\n")

    for user in users:

        username = user["UserName"]

        add_user_to_group(
            iam,
            username
        )

    print("\nCompleted.")
    print(
        "All IAM users are now members of the "
        f"{GROUP_NAME} group."
    )


if __name__ == "__main__":

    assign_readonly_to_all_users()