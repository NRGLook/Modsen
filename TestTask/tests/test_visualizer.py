import unittest

from PIL import Image

from TestTask.src.utils.visualizer import show_image, show_images


class TestVisualizer(unittest.TestCase):
    def setUp(self):
        """
        Set up a test image.
        """
        self.image = Image.new('RGB', (100, 100), color='red')
        self.images = [self.image for _ in range(4)]

    def test_show_image(self):
        """
        Test displaying a single image.
        """
        try:
            show_image(self.image, title="Test Image")
        except Exception as e:
            self.fail(f"show_image raised an exception: {e}")

    def test_show_images(self):
        """
        Test displaying a list of images.
        """
        try:
            show_images(
                self.images,
                titles=["Image 1", "Image 2", "Image 3", "Image 4"])
        except Exception as e:
            self.fail(f"show_images raised an exception: {e}")


if __name__ == '__main__':
    unittest.main()
