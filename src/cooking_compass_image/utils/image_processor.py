from io import BytesIO

from PIL import Image, UnidentifiedImageError


MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB
MAX_IMAGE_DIMENSION = 1920
WEBP_QUALITY = 82


class ImageProcessingError(Exception):
    """Raised when an uploaded image cannot be processed."""


def process_image(
    image_bytes: bytes,
) -> tuple[BytesIO, str, int, int, int]:
    """
    Validate, resize and compress an image.

    Returns:
        processed_file: processed image as BytesIO
        mime_type: output MIME type
        file_size: processed file size
        width: final width
        height: final height
    """

    # 1. Check whether the file is empty
    if not image_bytes:
        raise ImageProcessingError("Image file is empty.")

    # 2. Check original file size
    if len(image_bytes) > MAX_FILE_SIZE:
        raise ImageProcessingError(
            "Image size must not exceed 10 MB."
        )

    # 3. Open the image
    try:
        image = Image.open(BytesIO(image_bytes))

        # Verify that the file is actually a valid image
        image.verify()

    except UnidentifiedImageError:
        raise ImageProcessingError(
            "Uploaded file is not a valid image."
        )

    except Exception:
        raise ImageProcessingError(
            "Unable to process the uploaded image."
        )

    # 4. Re-open the image after verify()
    image = Image.open(BytesIO(image_bytes))

    # 5. Handle image modes
    if image.mode in ("RGBA", "LA", "P"):
        image = image.convert("RGBA")
    else:
        image = image.convert("RGB")

    # 6. Resize while maintaining aspect ratio
    image.thumbnail(
        (MAX_IMAGE_DIMENSION, MAX_IMAGE_DIMENSION),
        Image.Resampling.LANCZOS,
    )

    # 7. Compress and convert to WebP
    output = BytesIO()

    image.save(
        output,
        format="WEBP",
        quality=WEBP_QUALITY,
        method=6,
    )

    # Move cursor to beginning
    output.seek(0)

    # 8. Get final metadata
    width, height = image.size
    file_size = output.getbuffer().nbytes

    return (
        output,
        "image/webp",
        file_size,
        width,
        height,
    )