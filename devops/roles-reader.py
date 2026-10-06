import boto3
from botocore.exceptions import ClientError, NoCredentialsError


def list_iam_roles():
    try:
        iam = boto3.client("iam")

        paginator = iam.get_paginator("list_roles")

        print("\nAWS IAM ROLES")
        print("=" * 80)

        total_roles = 0

        for page in paginator.paginate():
            for role in page["Roles"]:
                total_roles += 1

                print(f"\nRole Name: {role['RoleName']}")
                print(f"ARN: {role['Arn']}")
                print(f"Path: {role['Path']}")
                print(f"Created: {role['CreateDate']}")
                print(
                    f"Max Session Duration: "
                    f"{role.get('MaxSessionDuration', 'N/A')} seconds"
                )
                print(f"Description: {role.get('Description', 'N/A')}")

        print("\n" + "=" * 80)
        print(f"Total IAM Roles: {total_roles}")

    except NoCredentialsError:
        print("AWS credentials were not found.")

    except ClientError as error:
        print(f"AWS error: {error}")

    except Exception as error:
        print(f"Unexpected error: {error}")


if __name__ == "__main__":
    list_iam_roles()