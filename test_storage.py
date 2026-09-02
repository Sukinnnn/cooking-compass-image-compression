from pathlib import Path

from cooking_compass_image.utils.storage_client import (
    upload_image,
    download_image,
    delete_image,
)


image_path = Path("test_images/test_output.webp")

image_bytes = image_path.read_bytes()

storage_key = "test/test_output.webp"


# Upload
print("Uploading...")

upload_image(
    image_bytes=image_bytes,
    storage_key=storage_key,
    mime_type="image/webp",
)

print("Upload successful!")


# Download
print("Downloading...")

downloaded_bytes = download_image(
    storage_key=storage_key,
)

print("Download successful!")
print("Downloaded size:", len(downloaded_bytes), "bytes")


# Verify downloaded data
if downloaded_bytes == image_bytes:
    print("Image verification successful!")
else:
    print("WARNING: Downloaded image differs from original!")


# Delete
print("Deleting...")

delete_image(
    storage_key=storage_key,
)

print("Delete successful!")