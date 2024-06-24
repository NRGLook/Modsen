import os
from typing import List, Tuple, Optional
from PIL import Image

from TestTask.src.utils.error_handler import handle_image_error


@handle_image_error
def load_images_from_directory(directory: str, supported_formats: Optional[Tuple[str, ...]] = None) -> List[Image.Image]:
    """
    Загружает изображения из указанной директории, поддерживая только указанные форматы.

    Args:
    directory (str): Путь к директории с изображениями.
    supported_formats (Optional[Tuple[str, ...]]): Кортеж поддерживаемых форматов изображений, по умолчанию поддерживаются JPEG, JPG, PNG, BMP, GIF.

    Returns:
    List[Image.Image]: Список объектов PIL.Image.
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
                print(f"Ошибка при загрузке изображения {filename}: {e}")
    return images
