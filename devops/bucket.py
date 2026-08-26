import boto3
from botocore.exceptions import ClientError, NoCredentialsError


BUCKET_NAME = "your-secure-bucket-name"
OBJECT_KEY = "test/example.txt"


def connect_to_s3():
    """
    Creates a secure connection to Amazon S3 using
    AWS credentials configured outside the application.
    """

    try:
        # boto3 uses HTTPS by default
        s3 = boto3.client(
            "s3",
            region_name="us-east-1"
        )

        # Verify that we can access the bucket
        s3.head_bucket(Bucket=BUCKET_NAME)

        print(f"Secure connection established to: {BUCKET_NAME}")
        return s3

    except NoCredentialsError:
        print("AWS credentials were not found.")
        return None

    except ClientError as e:
        print(f"AWS error: {e}")
        return None


def upload_file(s3, local_file):
    """Upload a file securely to S3."""

    try:
        s3.upload_file(
            local_file,
            BUCKET_NAME,
            OBJECT_KEY,
            ExtraArgs={
                "ServerSideEncryption": "AES256"
            }
        )

        print(f"Uploaded: {local_file}")
        print(f"s3://{BUCKET_NAME}/{OBJECT_KEY}")

    except ClientError as e:
        print(f"Upload failed: {e}")


def download_file(s3, local_file):
    """Download a file securely from S3."""

    try:
        s3.download_file(
            BUCKET_NAME,
            OBJECT_KEY,
            local_file
        )

        print(f"Downloaded to: {local_file}")

    except ClientError as e:
        print(f"Download failed: {e}")


if __name__ == "__main__":

    s3 = connect_to_s3()

    if s3:
        upload_file(s3, "example.txt")
        # download_file(s3, "downloaded_example.txt")