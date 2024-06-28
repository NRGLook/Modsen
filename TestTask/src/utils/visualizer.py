import matplotlib.pyplot as plt
from typing import List

from PIL import Image


def show_image(
        image: Image.Image,
        title: str = "Image"
) -> None:
    """
    Displays a single image with a title.

    Parameters:
        image (Image.Image):
            The image to display.
        title (str):
            The title of the image. Default is "Image".

    Example:
    >>> img = Image.open('example.jpg')
    >>> show_image(img, title='Example Image')
    """
    plt.figure(figsize=(6, 6))
    plt.imshow(image)
    plt.title(title)
    plt.axis('off')
    plt.show()


def show_images(
        images: List[Image.Image],
        titles: List[str] = None,
        cols: int = 3
) -> None:
    """
    Displays a list of images with titles.

    Parameters:
        images (List[Image.Image]):
            The list of images to display.
        titles (List[str]):
            The list of titles for each image. Default is None, which assigns
            an empty title to each image.
        cols (int):
            The number of images per row. Default is 3.

    Raises:
        AssertionError:
            If the number of images and titles do not match.

    Example:
    >>> imgs = [Image.open(f'image_{i}.jpg') for i in range(6)]
    >>> titles = [f'Image {i}' for i in range(6)]
    >>> show_images(imgs, titles, cols=2)
    """
    if titles is None:
        titles = [""] * len(images)
    assert len(images) == len(titles), \
        "The number of images and titles must match."

    rows = len(images) // cols + int(len(images) % cols > 0)
    plt.figure(figsize=(5 * cols, 5 * rows))
    for i, (image, title) in enumerate(zip(images, titles)):
        plt.subplot(rows, cols, i + 1)
        plt.imshow(image)
        plt.title(title)
        plt.axis('off')
    plt.tight_layout()
    plt.show()
