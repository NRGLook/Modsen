import os
from typing import List, Optional
from PIL import Image

from TestTask.src.utils.error_handler import handle_image_error


@handle_image_error
def save_image(image: Image.Image, directory: str, filename: str, format: Optional[str] = 'JPEG', quality: Optional[int] = 95) -> None:
    """
    Сохраняет одно изображение в указанной директории с заданными параметрами.

    Args:
    image (Image.Image): Объект изображения для сохранения.
    directory (str): Путь к директории, где будет сохранено изображение.
    filename (str): Имя файла, под которым изображение будет сохранено.
    format (Optional[str]): Формат файла изображения, например 'JPEG', 'PNG' и т.д.
    quality (Optional[int]): Качество сохранения изображения (используется только для форматов JPEG).
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
    image.save(os.path.join(directory, filename), format=format, quality=quality)


@handle_image_error
def save_images(images: List[Image.Image], directory: str, filenames: List[str], format: Optional[str] = 'JPEG', quality: Optional[int] = 95) -> None:
    """
    Сохраняет список изображений в указанной директории.

    Args:
    images (List[Image.Image]): Список изображений для сохранения.
    directory (str): Путь к директории, где будут сохранены изображения.
    filenames (List[str]): Список имен файлов, под которыми изображения будут сохранены.
    format (Optional[str]): Формат файла изображения.
    quality (Optional[int]): Качество сохранения изображения.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
    for img, fname in zip(images, filenames):
        img.save(os.path.join(directory, fname), format=format, quality=quality)
