import boto3

from cooking_compass_image.core.config import (
    B2_APPLICATION_KEY,
    B2_BUCKET_NAME,
    B2_ENDPOINT_URL,
    B2_KEY_ID,
)


s3_client = boto3.client(
    "s3",
    endpoint_url=B2_ENDPOINT_URL,
    aws_access_key_id=B2_KEY_ID,
    aws_secret_access_key=B2_APPLICATION_KEY,
    region_name="eu-central-003",
)


def upload_image(
    image_bytes: bytes,
    storage_key: str,
    mime_type: str,
) -> None:
    s3_client.put_object(
        Bucket=B2_BUCKET_NAME,
        Key=storage_key,
        Body=image_bytes,
        ContentType=mime_type,
    )


def download_image(storage_key: str) -> bytes:
    response = s3_client.get_object(
        Bucket=B2_BUCKET_NAME,
        Key=storage_key,
    )

    return response["Body"].read()


def delete_image(storage_key: str) -> None:
    s3_client.delete_object(
        Bucket=B2_BUCKET_NAME,
        Key=storage_key,
    )