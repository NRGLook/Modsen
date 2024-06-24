from typing import List
from PIL import Image
import matplotlib.pyplot as plt


def show_image(image: Image.Image, title: str = "Image") -> None:
    """
    Отображает одно изображение с заголовком.

    Args:
    image (Image.Image): Изображение для отображения.
    title (str): Заголовок изображения.
    """
    plt.figure(figsize=(6, 6))
    plt.imshow(image)
    plt.title(title)
    plt.axis('off')
    plt.show()


def show_images(images: List[Image.Image], titles: List[str] = None, cols: int = 3) -> None:
    """
    Отображает список изображений с заголовками.

    Args:
    images (List[Image.Image]): Список изображений для отображения.
    titles (List[str]): Список заголовков для каждого изображения.
    cols (int): Количество изображений в одной строке.
    """
    if titles is None:
        titles = [""] * len(images)
    assert len(images) == len(titles), "Количество изображений и заголовков должно совпадать."

    rows = len(images) // cols + int(len(images) % cols > 0)
    plt.figure(figsize=(5 * cols, 5 * rows))
    for i, (image, title) in enumerate(zip(images, titles)):
        plt.subplot(rows, cols, i + 1)
        plt.imshow(image)
        plt.title(title)
        plt.axis('off')
    plt.tight_layout()
    plt.show()
