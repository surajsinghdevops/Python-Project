import boto3
import os

from botocore.exceptions import ClientError

from config.config import AWS_REGION
from config.config import S3_BUCKET


s3 = boto3.client(
    "s3",
    region_name=AWS_REGION
)


def upload_reports():

    report_folder = "reports"

    uploaded = 0

    try:

        for file in os.listdir(report_folder):

            file_path = os.path.join(
                report_folder,
                file
            )

            print(f"Uploading {file}...")

            s3.upload_file(
                file_path,
                S3_BUCKET,
                file
            )

            uploaded += 1

        print(f"\n✓ {uploaded} reports uploaded successfully.")

    except ClientError as error:

        print(f"\nS3 Upload Failed:\n{error}")
