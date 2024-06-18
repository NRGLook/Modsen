# Image Augmentation Tool

This project is a GUI tool for augmenting images using various transformations. The tool is built with Python and uses libraries such as OpenCV, Pillow, and albumentations for image processing and augmentation.

## Features

- Load images from a specified directory
- Apply various augmentations (resize, crop, rotate, flip, brightness/contrast adjustment, blur)
- Save augmented images to a specified directory
- Configure augmentation parameters via GUI

## Installation

1. Clone the repository:
    ```
    git clone https://github.com/yourusername/image_augmentation_tool.git
    ```

2. Navigate to the project directory:
    ```
    cd image_augmentation_tool
    ```

3. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:
    ```
    python src/main.py
    ```

2. Use the GUI to specify input and output directories, configure augmentation parameters, and start the augmentation process.

## Project Structure

- `images/` - Directory for storing input and output images
- `src/` - Source code directory
  - `__init__.py` - Initialization file for the source code package
  - `augmentations.py` - Contains functions for loading, augmenting, and saving images
  - `gui.py` - Contains the GUI implementation using tkinter
  - `main.py` - Entry point for the application

## License

This project is licensed under the MIT License.
