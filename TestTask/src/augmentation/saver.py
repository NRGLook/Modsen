import os
from typing import List, Optional
from PIL import Image


def save_image(
        image: Image.Image,
        directory: str,
        filename: str,
        format_image: Optional[str] = None,
        quality: Optional[int] = 95
) -> None:
    """
    Saves a single image to the specified directory with the given parameters.

    Args:
        image (Image.Image):
            The image object to be saved.
        directory (str):
            The path to the directory where the image will be saved.
        filename (str):
            The name of the file under which the image will be saved.
        format_image (Optional[str]):
            The file format of the image, such as 'JPEG', 'PNG', 'BMP', 'GIF'.
        quality (Optional[int]):
            The quality for saving the image (used only for JPEG format).
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

    if format_image is None:
        format_image = filename.split('.')[-1].upper()

    if format_image == 'JPG':
        format_image = 'JPEG'

    save_params = {
        'format': format_image
    }

    if format_image.upper() == 'JPEG':
        save_params['quality'] = quality

    image.save(
        os.path.join(directory, filename),
        **save_params
    )


def save_images(
        images: List[Image.Image],
        directory: str,
        filenames: List[str],
        format_image: Optional[str] = None,
        quality: Optional[int] = 95
) -> None:
    """
    Saves a list of images to the specified directory.

    Args:
        images (List[Image.Image]):
            The list of images to be saved.
        directory (str):
            The path to the directory where the images will be saved.
        filenames (List[str]):
            The list of filenames under which the images will be saved.
        format_image (Optional[str]):
            The file format of the images, such as 'JPEG', 'PNG', 'BMP', 'GIF'.
        quality (Optional[int]):
            The quality for saving the images (used only for JPEG format).
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

    for img, fname in zip(images, filenames):
        format_img = format_image if format_image else fname.split('.')[
            -1].upper()

        if format_img == 'JPG':
            format_img = 'JPEG'

        save_params = {
            'format': format_img
        }

        if save_params['format'] == 'JPEG':
            save_params['quality'] = quality

        img.save(
            os.path.join(directory, fname),
            **save_params
        )
