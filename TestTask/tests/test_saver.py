import unittest
import os

from unittest.mock import patch

from PIL import Image

from TestTask.src.augmentation.image_saver import save_image, save_images


class TestSaver(unittest.TestCase):
    def setUp(self):
        """
        Set up a test directory and images.
        """
        self.test_dir = 'test_save_images'
        os.makedirs(self.test_dir, exist_ok=True)
        self.image = Image.new('RGB', (100, 100))
        self.formats = ['JPEG', 'PNG', 'BMP', 'GIF']

    def tearDown(self):
        """
        Tear down the test directory and images.
        """
        for filename in os.listdir(self.test_dir):
            file_path = os.path.join(self.test_dir, filename)
            os.remove(file_path)
        os.rmdir(self.test_dir)

    def test_save_image_all_formats(self):
        """
        Test saving a single image in all supported formats.
        """
        for fmt in self.formats:
            save_path = os.path.join(self.test_dir,
                                     f'saved_image.{fmt.lower()}')
            save_image(self.image, self.test_dir,
                       f'saved_image.{fmt.lower()}', format_image=fmt)
            self.assertTrue(os.path.exists(save_path))

    def test_save_images_all_formats(self):
        """
        Test saving multiple images in all supported formats.
        """
        for fmt in self.formats:
            images = [self.image for _ in range(3)]
            filenames = [f'saved_image_{i}.{fmt.lower()}' for i in range(3)]
            save_images(images, self.test_dir, filenames, format_image=fmt)
            for fname in filenames:
                self.assertTrue(os.path.exists(os.path.join(
                    self.test_dir,
                    fname)))

    def test_save_image_default_format(self):
        """
        Test saving a single image without specifying format explicitly.
        """
        save_path = os.path.join(self.test_dir, 'saved_image.jpg')
        save_image(self.image, self.test_dir, 'saved_image.jpg')
        self.assertTrue(os.path.exists(save_path))

    def test_save_images_default_format(self):
        """
        Test saving multiple images without specifying format explicitly.
        """
        images = [self.image for _ in range(3)]
        filenames = [f'saved_image_{i}.jpg' for i in range(3)]
        save_images(images, self.test_dir, filenames)
        for fname in filenames:
            self.assertTrue(os.path.exists(os.path.join(self.test_dir, fname)))


if __name__ == '__main__':
    unittest.main()
