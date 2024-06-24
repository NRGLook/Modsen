import random
from typing import Tuple, List
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter, ImageOps, ImageDraw

from TestTask.src.utils.error_handler import handle_image_error


@handle_image_error
def resize_image(image: Image.Image, size: Tuple[int, int] = (256, 256)) -> Image.Image:
    """ Изменяет размер изображения. """
    return image.resize(size, Image.ANTIALIAS)


@handle_image_error
def rotate_image(image: Image.Image, degrees: int = 90) -> Image.Image:
    """ Поворачивает изображение на заданное количество градусов. """
    return image.rotate(degrees)


@handle_image_error
def flip_image(image: Image.Image, mode: str = 'horizontal') -> Image.Image:
    """ Отражает изображение по горизонтали или вертикали. """
    if mode == 'horizontal':
        return image.transpose(Image.FLIP_LEFT_RIGHT)
    else:
        return image.transpose(Image.FLIP_TOP_BOTTOM)


@handle_image_error
def change_brightness(image: Image.Image, factor: float = 1.5) -> Image.Image:
    """ Изменяет яркость изображения. """
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(factor)


@handle_image_error
def change_contrast(image: Image.Image, factor: float = 1.5) -> Image.Image:
    """ Изменяет контраст изображения. """
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(factor)


@handle_image_error
def add_noise(image: Image.Image, amount: float = 0.02) -> Image.Image:
    """ Добавляет случайный шум к изображению. """
    np_image = np.array(image)
    noise = np.random.normal(0, 255 * amount, np_image.shape)
    noisy_image = np.clip(np_image + noise, 0, 255).astype(np.uint8)
    return Image.fromarray(noisy_image)


@handle_image_error
def shift_image(image: Image.Image, shift: Tuple[int, int] = (10, 10)) -> Image.Image:
    """ Сдвигает изображение. """
    return ImageOps.offset(image, *shift)


@handle_image_error
def random_crop(image: Image.Image, size: Tuple[int, int] = (100, 100)) -> Image.Image:
    """ Выполняет случайную обрезку изображения. """
    width, height = image.size
    left = random.randint(0, width - size[0])
    top = random.randint(0, height - size[1])
    return image.crop((left, top, left + size[0], top + size[1]))


@handle_image_error
def overlay_text(image: Image.Image, text: str = "Sample Text", position: Tuple[int, int] = (50, 50), color: Tuple[int, int, int] = (255, 255, 255)) -> Image.Image:
    """ Наложение текста на изображение. """
    draw = ImageDraw.Draw(image)
    draw.text(position, text, fill=color)
    return image


@handle_image_error
def overlay_image(main_image: Image.Image, overlay: Image.Image, position: Tuple[int, int] = (0, 0), transparency: float = 0.5) -> Image.Image:
    """ Наложение другого изображения с заданной прозрачностью. """
    overlay = overlay.resize(main_image.size)
    mask = Image.new("L", main_image.size, int(255 * transparency))
    return Image.composite(main_image, overlay, mask)
