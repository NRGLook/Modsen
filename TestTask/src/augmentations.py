import os
import cv2
from albumentations import (
    Compose,
    Resize,
    RandomCrop,
    Rotate,
    Flip,
    RandomBrightnessContrast,
    GaussianBlur
)


def load_images_from_directory(
        directory,
        formats=('jpg', 'jpeg')
):
    images = []
    filenames = []
    for filename in os.listdir(directory):
        if filename.lower().endswith(formats):
            img_path = os.path.join(directory, filename)
            img = cv2.imread(img_path)
            if img is not None:
                images.append(img)
                filenames.append(filename)
    return images, filenames


def save_images_to_directory(
        images,
        filenames,
        directory,
        prefix='aug'
):
    if not os.path.exists(directory):
        os.makedirs(directory)
    for idx, img in enumerate(images):
        save_path = os.path.join(directory, f"{prefix}_{filenames[idx]}")
        cv2.imwrite(save_path, img)


def apply_augmentations(
        images,
        resize_size=(256, 256),
        crop_size=(200, 200),
        rotate_limit=45,
        flip_prob=0.5,
        brightness_contrast_prob=0.2,
        blur_prob=0.1
):
    transform = Compose([
        Resize(*resize_size),
        RandomCrop(*crop_size),
        Rotate(limit=rotate_limit),
        Flip(p=flip_prob),
        RandomBrightnessContrast(p=brightness_contrast_prob),
        GaussianBlur(p=blur_prob)
    ])

    augmented_images = []
    for img in images:
        augmented = transform(image=img)['image']
        augmented_images.append(augmented)
    return augmented_images
