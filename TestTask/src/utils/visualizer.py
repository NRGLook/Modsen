from typing import List

from PIL import Image

import matplotlib.pyplot as plt


def show_image(
        image: Image.Image,
        title: str = "Image"
) -> None:
    """
    Displays a single image with a title.

    Args:
        image (Image.Image): The image to display.
        title (str): The title of the image.
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

    Args:
        images (List[Image.Image]): The list of images to display.
        titles (List[str]): The list of titles for each image.
        cols (int): The number of images per row.
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
