# Image Augmentation Tool

This project is a GUI tool for augmenting images using various transformations. 
The tool is built with Python and uses libraries such as OpenCV, Pillow, 
and albumentations for image processing and augmentation.

## Full condition

Техническое задание по аугментации изображений

Введение

Цель этого задания - написать программу, которая сможет выполнять аугментацию
изображений, используемых для задач машинного обучения, например, классификации
изображений. Программа должна уметь применять различные преобразования к 
изображениям для увеличения размера обучающего набора данных и улучшения 
обобщающей способности моделей. Программа должна быть реализована на языке 
Python и предоставлять широкий спектр преобразований с возможностью настройки 
параметров.

Требования

1. Загрузка данных:
Программа должна поддерживать загрузку изображений из указанных
директорий.
Поддерживаемые формат изображений: JPEG.
2. Преобразования изображений:
Программа должна реализовывать следующие базовые преобразования:
Изменение размера (масштабирование, обрезка)
Повороты и отражения
3. Вывод результатов:
Программа должна создавать заданное число преобразованных
изображений и сохранять их в указанную директорию.
Пользователь должен иметь возможность настраивать параметры
преобразований.

Среда разработки

1. Язык программирования: Python 3.x
2. Рекомендуемые библиотеки и инструменты:
numpy, pandas для работы с данными.
opencv, PIL для обработки изображений.
matplotlib для визуализации.

Бонусы реализации (Опционально)

Поддержка дополнительных форматов изображений: PNG, BMP, GIF.
Поддержка дополнительных преобразований изображений:
1) Изменение яркости, контрастности, насыщенности
2) Добавление шума
3) Геометрические преобразования (сдвиг, наклон, растяжение)
4) Случайные вырезки (random crops)
5) Наложение текста или других изображений
6) Создание искусственных изображений помощью генеративного ИИ
7) Обработка ошибок для случаев некорректных или поврежденных изображений.
8) Визуализация преобразований.
9) Поддержка параллельной обработки для ускорения процесса.
10) Функциональные тесты.
11) Изучение библиотек для аугментации изображений albumentations, imgaug,
augmentor.


## Features

- Load images from a specified directory
- Apply various image transformations(with JPEG, BMP, PNG):
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
  - `augmentation/` - Directory containing augmentation related code
    - `loader.py` - Functions for loading images from a directory
    - `transformer.py` - Functions for applying various transformations to images
    - `saver.py` - Functions for saving images to a directory
  - `utils/` - Directory containing augmentation related code
    - `error_handler.py` - Base exceptions
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

2. Use the GUI to specify input and output directories, configure augmentation 
parameters, and start the augmentation process.


## License

This project is licensed under the MIT License.
