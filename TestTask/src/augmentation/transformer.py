import random
import numpy as np
from typing import Tuple

from PIL import Image, ImageEnhance, ImageDraw, ImageChops, ImageFont

from TestTask.src.utils.error_handler import handle_image_error


@handle_image_error
def resize_image(
        image: Image.Image,
        size: Tuple[int, int] = (256, 256)
) -> Image.Image:
    """
    Resizes the image to the given size.

    Parameters:
    image (Image.Image): The original image.
    size (Tuple[int, int]): The new size of the image (width, height).

    Returns:
    Image.Image: The resized image.

    Raises:
    ValueError: If the provided size is not a tuple of two integers.

    Example:
    >>> img = Image.open('example.jpg')
    >>> resized_img = resize_image(img, (100, 100))
    >>> resized_img.size
    (100, 100)
    """
    return image.resize(size, Image.Resampling.LANCZOS)


@handle_image_error
def rotate_image(
        image: Image.Image,
        degrees: int = 90
) -> Image.Image:
    """
    Rotates the image by a given number of degrees.

    Parameters:
    image (Image.Image): The original image.
    degrees (int): The number of degrees to rotate the image.

    Returns:
    Image.Image: The rotated image.

    Example:
    >>> img = Image.open('example.jpg')
    >>> rotated_img = rotate_image(img, 45)
    >>> rotated_img.show()
    """
    return image.rotate(degrees, expand=True)


@handle_image_error
def flip_image(
        image: Image.Image,
        mode: str = 'horizontal'
) -> Image.Image:
    """
    Flips the image horizontally or vertically.

    Parameters:
    image (Image.Image): The original image.
    mode (str): The mode of flipping ('horizontal' or 'vertical').

    Returns:
    Image.Image: The flipped image.

    Raises:
    ValueError: If the mode is not 'horizontal' or 'vertical'.

    Example:
    >>> img = Image.open('example.jpg')
    >>> flipped_img = flip_image(img, 'vertical')
    >>> flipped_img.show()
    """
    if mode == 'horizontal':
        return image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    elif mode == 'vertical':
        return image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    else:
        raise ValueError("Mode should be 'horizontal' or 'vertical'")


@handle_image_error
def change_brightness(
        image: Image.Image,
        factor: float = 1.5
) -> Image.Image:
    """
    Changes the brightness of the image.

    Parameters:
    image (Image.Image): The original image.
    factor (float): The factor by which to change the brightness.

    Returns:
    Image.Image: The image with changed brightness.

    Example:
    >>> img = Image.open('example.jpg')
    >>> bright_img = change_brightness(img, 1.2)
    >>> bright_img.show()
    """
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(factor)


@handle_image_error
def change_contrast(
        image: Image.Image,
        factor: float = 1.5
) -> Image.Image:
    """
    Changes the contrast of the image.

    Parameters:
    image (Image.Image): The original image.
    factor (float): The factor by which to change the contrast.

    Returns:
    Image.Image: The image with changed contrast.

    Example:
    >>> img = Image.open('example.jpg')
    >>> contrast_img = change_contrast(img, 1.8)
    >>> contrast_img.show()
    """
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(factor)


@handle_image_error
def add_noise(
        image: Image.Image,
        amount: float = 0.02
) -> Image.Image:
    """
    Adds random noise to the image.

    Parameters:
    image (Image.Image): The original image.
    amount (float): The amount of noise to add.

    Returns:
    Image.Image: The image with added noise.

    Example:
    >>> img = Image.open('example.jpg')
    >>> noisy_img = add_noise(img, 0.05)
    >>> noisy_img.show()
    """
    np_image = np.array(image)
    noise = np.random.normal(0, 255 * amount, np_image.shape)
    noisy_image = np.clip(np_image + noise, 0, 255).astype(np.uint8)
    return Image.fromarray(noisy_image)


@handle_image_error
def shift_image(
        image: Image.Image,
        shift: Tuple[int, int] = (10, 10)
) -> Image.Image:
    """
    Shifts the image by a given amount.

    Parameters:
    image (Image.Image): The original image.
    shift (Tuple[int, int]): The amount to shift the image (x, y).

    Returns:
    Image.Image: The shifted image.

    Example:
    >>> img = Image.open('example.jpg')
    >>> shifted_img = shift_image(img, (20, 30))
    >>> shifted_img.show()
    """
    return ImageChops.offset(image, shift[0], shift[1])


@handle_image_error
def random_crop(
        image: Image.Image,
        size: Tuple[int, int] = (100, 100)
) -> Image.Image:
    """
    Performs a random crop on the image.

    Parameters:
    image (Image.Image): The original image.
    size (Tuple[int, int]): The size of the crop (width, height).

    Returns:
    Image.Image: The cropped image.

    Raises:
    ValueError: If the crop size is larger than the original image size.

    Example:
    >>> img = Image.open('example.jpg')
    >>> cropped_img = random_crop(img, (50, 50))
    >>> cropped_img.show()
    """
    width, height = image.size
    crop_width, crop_height = size

    if crop_width > width or crop_height > height:
        raise ValueError("Crop size must be smaller than the original image size")

    left = random.randint(0, width - crop_width)
    top = random.randint(0, height - crop_height)
    return image.crop((left, top, left + crop_width, top + crop_height))


@handle_image_error
def overlay_text(
        image: Image.Image,
        text: str = "Sample Text",
        position: Tuple[int, int] = (50, 50),
        color: Tuple[int, int, int, int] = (255, 255, 255, 255)
) -> Image.Image:
    """
    Overlays text on the image.

    Parameters:
    image (Image.Image): The original image.
    text (str): The text to overlay.
    position (Tuple[int, int]): The position to place the text.
    color (Tuple[int, int, int, int]): The color of the text, including alpha.

    Returns:
    Image.Image: The image with overlaid text.

    Example:
    >>> img = Image.open('example.jpg')
    >>> text_img = overlay_text(img, "Hello", (100, 100), (255, 0, 0, 255))
    >>> text_img.show()
    """
    try:
        draw = ImageDraw.Draw(image)
        font = ImageFont.load_default()
        draw.text(position, text, fill=color, font=font)
        return image
    except Exception as e:
        print(f"Error overlaying text: {e}")
        return None


@handle_image_error
def overlay_image(
        main_image: Image.Image,
        overlay: Image.Image,
        position: Tuple[int, int] = (0, 0),
        transparency: float = 0.5
) -> Image.Image:
    """
    Overlays another image with the given transparency.

    Parameters:
    main_image (Image.Image): The original image.
    overlay (Image.Image): The overlay image.
    position (Tuple[int, int]): The position to place the overlay image.
    transparency (float): The transparency level of the overlay image.

    Returns:
    Image.Image: The image with overlaid image.

    Example:
    >>> main_img = Image.open('main.jpg')
    >>> overlay_img = Image.open('overlay.png')
    >>> combined_img = overlay_image(main_img, overlay_img, (50, 50), 0.7)
    >>> combined_img.show()
    """
    overlay = overlay.resize(main_image.size)
    overlay_with_transparency = overlay.copy()
    overlay_with_transparency.putalpha(int(255 * transparency))

    # Create a blank image with an alpha channel (RGBA)
    combined = Image.new("RGBA", main_image.size)
    combined.paste(main_image, (0, 0))
    combined.paste(
        overlay_with_transparency,
        position,
        overlay_with_transparency
    )

    return combined.convert("RGB")
