# Image Augmentation Tool

This project is a GUI tool for augmenting images using various transformations. The tool is built with Python and uses libraries such as OpenCV, Pillow, and albumentations for image processing and augmentation.

## Full Condition

### Image Augmentation Technical Specification

#### Introduction

The goal of this task is to write a program capable of performing image augmentation, which is used in machine learning tasks such as image classification. The program should be able to apply various transformations to images to increase the size of the training dataset and improve the generalization ability of models. The program must be implemented in Python and provide a wide range of transformations with adjustable parameters.

#### Requirements

1. **Data Loading:**
   - The program must support loading images from specified directories.
   - Supported image formats: JPEG, PNG, BMP, GIF.

2. **Image Transformations:**
   - The program must implement the following basic transformations:
     - Resize (scaling, cropping)
     - Rotations and reflections

3. **Output Results:**
   - The program must create a specified number of transformed images and save them to the specified directory.
   - Users must be able to customize the parameters of the transformations.

#### Development Environment

1. **Programming Language:**
   - Python 3.x

2. **Recommended Libraries and Tools:**
   - numpy, pandas for data manipulation.
   - opencv, PIL for image processing.
   - matplotlib for visualization.

#### Optional Enhancements

Support for additional image formats: PNG, BMP, GIF.

Support for additional image transformations:
1. Brightness, contrast, saturation adjustment
2. Adding noise
3. Geometric transformations (shifting, tilting, stretching)
4. Random crops
5. Overlaying text or other images
6. Generating artificial images using generative AI
7. Error handling for incorrect or corrupted images
8. Visualization of transformations
9. Support for parallel processing to speed up the process
10. Functional tests
11. Exploration of image augmentation libraries: albumentations, imgaug, augmentor

## Features

- Load images from a specified directory
- Apply various image transformations (with JPEG, BMP, PNG):
  - Resize (scaling, cropping)
  - Rotate
  - Flip (horizontal, vertical)
  - Change brightness and contrast
  - Add noise
  - Geometric transformations (shift)
  - Random crops (crop width, crop height)
  - Overlay text
  - Overlay images
- Save transformed images to a specified directory
- Functional tests

## Project Structure

- `data/` - Directory for storing input and output images
- `src/` - Source code directory
  - `augmentation/` - Directory containing augmentation-related code
    - `loader.py` - Functions for loading images from a directory
    - `transformer.py` - Functions for applying various transformations to images
    - `saver.py` - Functions for saving images to a directory
  - `utils/` - Directory containing utility code
    - `error_handler.py` - Functions for handling and logging errors
    - `visualizer.py` - Functions for visualizing images
  - `gui.py` - Contains the GUI implementation using Tkinter
  - `main.py` - Entry point for the application
- `tests/` - Directory containing test cases
  - `test_loader.py` - Test cases for `loader.py`
  - `test_transformer.py` - Test cases for `transformer.py`
  - `test_saver.py` - Test cases for `saver.py`
- `requirements.txt` - File listing required Python packages
- `TaskCondition.md` - Project documentation and instructions

## Installation

1. Clone the repository:
    ```
    git clone https://github.com/NRGLook/Modsen.git
    ```

2. Navigate to the project directory:
    ```
    cd TestTask
    ```

3. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:
    ```
    python TestTask/src/main.py
    ```

2. Use the GUI to specify input and output directories, configure augmentation parameters, and start the augmentation process.


## To-Do

- [ ] Add advanced functionality for image augmentation from libraries such as albumentations, imgaug, and augmentor. Compare the performance of these libraries with each other.
- [ ] Create artificial images using generative AI.


## License

This project is licensed under the MIT License.
