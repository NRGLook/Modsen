import os
from typing import List, Tuple, Optional

from PIL import Image

from TestTask.src.utils.error_handler import handle_image_error


@handle_image_error
def load_images_from_directory(
        directory: str,
        supported_formats: Optional[Tuple[str, ...]] = None
) -> List[Image.Image]:
    """
    Loads images from the specified directory, supporting only the specified
    formats.

    Args:
        directory (str):
            The path to the directory containing images.
        supported_formats (Optional[Tuple[str, ...]]):
            A tuple of supported image formats. Defaults to JPEG, JPG, PNG,
            BMP, GIF.

    Returns:
        List[Image.Image]: A list of PIL.Image objects.
    """
    if supported_formats is None:
        supported_formats = ('.jpeg', '.jpg', '.png', '.bmp', '.gif')

    images = []
    for filename in os.listdir(directory):
        if filename.lower().endswith(supported_formats):
            try:
                img_path = os.path.join(directory, filename)
                with Image.open(img_path) as img:
                    images.append(img.copy())
            except IOError as e:
                print(f"Error loading image {filename}: {e}")
    return images
