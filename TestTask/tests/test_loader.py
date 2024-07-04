import unittest
import os

from PIL import Image, UnidentifiedImageError

from TestTask.src.augmentation.image_loader import load_images_from_directory


class TestLoader(unittest.TestCase):
    def setUp(self):
        """
        Set up test directories and images.
        """
        self.test_dir = 'test_images'
        os.makedirs(self.test_dir, exist_ok=True)
        self.image_path = os.path.join(self.test_dir, 'test_image.jpg')
        Image.new('RGB', (100, 100)).save(self.image_path)

        self.empty_dir = 'empty_test_images'
        os.makedirs(self.empty_dir, exist_ok=True)

        self.unsupported_dir = 'unsupported_images'
        os.makedirs(self.unsupported_dir, exist_ok=True)
        self.unsupported_image_path = os.path.join(
            self.unsupported_dir,
            'test_image.txt'
        )
        with open(self.unsupported_image_path, 'w') as f:
            f.write("This is a test file, not an image.")

        self.corrupted_dir = 'corrupted_images'
        os.makedirs(self.corrupted_dir, exist_ok=True)
        self.corrupted_image_path = os.path.join(
            self.corrupted_dir,
            'corrupted_image.jpg'
        )
        with open(self.corrupted_image_path, 'wb') as f:
            f.write(b"This is not a valid image file content.")

    def tearDown(self):
        """
        Tear down test directories and images.
        """
        for dir_path in [
            self.test_dir,
            self.empty_dir,
            self.unsupported_dir,
            self.corrupted_dir
        ]:
            for filename in os.listdir(dir_path):
                file_path = os.path.join(dir_path, filename)
                os.remove(file_path)
            os.rmdir(dir_path)

    def test_load_images_from_directory(self):
        """
        Test loading images from a directory.
        """
        images = load_images_from_directory(self.test_dir)
        self.assertEqual(len(images), 1)
        self.assertIsInstance(images[0], Image.Image)

    def test_load_images_from_empty_directory(self):
        """
        Test loading images from an empty directory.
        """
        images = load_images_from_directory(self.empty_dir)
        self.assertEqual(len(images), 0)

    def test_load_unsupported_images_from_directory(self):
        """
        Test loading unsupported format images from a directory.
        """
        images = load_images_from_directory(self.unsupported_dir)
        self.assertEqual(len(images), 0)

    def test_load_corrupted_images_from_directory(self):
        """
        Test loading corrupted images from a directory.
        """
        images = load_images_from_directory(self.corrupted_dir)
        self.assertEqual(len(images), 0)

    def test_load_multiple_formats_from_directory(self):
        """
        Test loading images with different supported formats from a directory.
        """
        for fmt in ['PNG', 'BMP', 'GIF']:
            Image.new(
                'RGB',
                (100, 100)).save(
                os.path.join(self.test_dir, f'test_image.{fmt.lower()}')
            )

        images = load_images_from_directory(self.test_dir)
        self.assertEqual(len(images), 4)  # 1 JPG + 3 additional formats
        for img in images:
            self.assertIsInstance(img, Image.Image)


if __name__ == '__main__':
    unittest.main()
