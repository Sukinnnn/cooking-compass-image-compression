from pathlib import Path
from time import perf_counter

from cooking_compass_image.utils.image_processor import process_image


def format_size(size_in_bytes: int) -> str:
    if size_in_bytes >= 1024 * 1024:
        return f"{size_in_bytes / (1024 * 1024):.2f} MB"

    return f"{size_in_bytes / 1024:.2f} KB"


image_path = next(
    (
        p
        for p in Path("test_images").iterdir()
        if p.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp"}
    )
)

original_bytes = image_path.read_bytes()
original_size = len(original_bytes)

print(f"Original size: {format_size(original_size)}")


start_time = perf_counter()

processed_file, mime_type, file_size, width, height = process_image(
    original_bytes
)

end_time = perf_counter()

processing_time = end_time - start_time

size_reduction = (
    (original_size - file_size) / original_size
) * 100


output_path = Path("test_images/test_output.webp")
output_path.write_bytes(processed_file.read())


print(f"Processed MIME type: {mime_type}")
print(f"Processed size: {format_size(file_size)}")
print(f"Final dimensions: {width} x {height}")
print(f"Compression time: {processing_time:.4f} seconds")
print(f"Size reduction: {size_reduction:.2f}%")
print(f"Saved: {output_path}")