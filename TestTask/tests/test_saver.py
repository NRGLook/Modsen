import unittest
import os
from unittest.mock import patch
from PIL import Image
from TestTask.src.augmentation.saver import save_image, save_images


class TestSaver(unittest.TestCase):
    def setUp(self):
        """
        Set up a test directory and images.
        """
        self.test_dir = 'test_save_images'
        os.makedirs(self.test_dir, exist_ok=True)
        self.image = Image.new('RGB', (100, 100))

    def tearDown(self):
        """
        Tear down the test directory and images.
        """
        for filename in os.listdir(self.test_dir):
            file_path = os.path.join(self.test_dir, filename)
            os.remove(file_path)
        os.rmdir(self.test_dir)

    def test_save_image(self):
        """
        Test saving a single image.
        """
        save_path = os.path.join(self.test_dir, 'saved_image.jpg')
        save_image(self.image, self.test_dir, 'saved_image.jpg')
        self.assertTrue(os.path.exists(save_path))

    @patch('PIL.Image.Image.save', side_effect=OSError)
    def test_save_image_invalid_directory(self, mock_save):
        """
        Test handling error when saving an image to an invalid directory.
        """
        with self.assertRaises(OSError):
            save_image(
                self.image,
                'invalid_dir',
                'saved_image.jpg'
            )

    def test_save_images(self):
        """
        Test saving a list of images.
        """
        images = [self.image for _ in range(3)]
        filenames = [f'saved_image_{i}.jpg' for i in range(3)]
        save_images(images, self.test_dir, filenames)
        for fname in filenames:
            self.assertTrue(os.path.exists(os.path.join(self.test_dir, fname)))

    @patch('PIL.Image.Image.save', side_effect=OSError)
    def test_save_images_invalid_directory(self, mock_save):
        """
        Test handling error when saving a list of images to an
        invalid directory.
        """
        images = [self.image for _ in range(3)]


if __name__ == '__main__':
    unittest.main()
