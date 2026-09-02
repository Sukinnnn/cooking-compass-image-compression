import os

from dotenv import load_dotenv


load_dotenv()


B2_KEY_ID = os.getenv("B2_KEY_ID")
B2_APPLICATION_KEY = os.getenv("B2_APPLICATION_KEY")
B2_BUCKET_NAME = os.getenv("B2_BUCKET_NAME")
B2_ENDPOINT_URL = os.getenv("B2_ENDPOINT_URL")


if not all(
    [
        B2_KEY_ID,
        B2_APPLICATION_KEY,
        B2_BUCKET_NAME,
        B2_ENDPOINT_URL,
    ]
):
    raise RuntimeError(
        "Backblaze configuration is incomplete. "
        "Check your .env file."
    )