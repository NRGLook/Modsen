import os
from typing import List, Optional
from PIL import Image

from TestTask.src.utils.error_handler import handle_image_error


@handle_image_error
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
    if image is None:
        raise ValueError("Cannot save a None image.")

    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
        except PermissionError as e:
            raise PermissionError(f"Permission denied: {e}")

    if format_image is None:
        format_image = filename.split('.')[-1].upper()

    # Convert JPG to JPEG
    if format_image.upper() == 'JPG':
        format_image = 'JPEG'

    # Convert images with mode 'P' or 'RGBA' to 'RGB'
    if format_image.upper() in ['JPEG', 'JPG'] and image.mode in ['P', 'RGBA']:
        image = image.convert('RGB')

    save_params = {
        'format': format_image
    }

    if format_image.upper() in ['JPEG', 'JPG']:
        save_params['quality'] = quality

    try:
        image.save(
            os.path.join(directory, filename),
            **save_params
        )
    except KeyError:
        raise ValueError(f"Unsupported format: {format_image}")
    except PermissionError as e:
        raise PermissionError(f"Permission denied: {e}")


@handle_image_error
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
        try:
            os.makedirs(directory)
        except PermissionError as e:
            raise PermissionError(f"Permission denied: {e}")

    for img, fname in zip(images, filenames):
        if img is None:
            raise ValueError("Cannot save a None image.")

        if format_image is None:
            format_image = fname.split('.')[-1].upper()

        # Convert JPG to JPEG
        if format_image.upper() == 'JPG':
            format_image = 'JPEG'

        # Convert images with mode 'P' or 'RGBA' to 'RGB'
        if format_image.upper() in ['JPEG', 'JPG'] and img.mode in ['P',
                                                                    'RGBA']:
            img = img.convert('RGB')

        save_params = {
            'format': format_image
        }

        if save_params['format'] in ['JPEG', 'JPG']:
            save_params['quality'] = quality

        try:
            img.save(
                os.path.join(directory, fname),
                **save_params
            )
        except KeyError:
            raise ValueError(f"Unsupported format: {format_image}")
        except PermissionError as e:
            raise PermissionError(f"Permission denied: {e}")
