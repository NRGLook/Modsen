import unittest

from TestTask.src.augmentation.transformer import *


class TestTransformer(unittest.TestCase):
    def setUp(self):
        """
        Set up a test image.
        """
        self.image = Image.new('RGB', (100, 100), color='red')

    def test_resize_image(self):
        """
        Test resizing an image.
        """
        resized_image = resize_image(self.image, size=(50, 50))
        self.assertIsNotNone(resized_image)
        self.assertEqual(resized_image.size, (50, 50))

    def test_rotate_image(self):
        """
        Test rotating an image.
        """
        rotated_image = rotate_image(self.image, degrees=45)
        self.assertIsNotNone(rotated_image)
        self.assertIsInstance(rotated_image, Image.Image)

    def test_flip_image(self):
        """
        Test flipping an image.
        """
        flipped_image = flip_image(self.image, mode='horizontal')
        self.assertIsNotNone(flipped_image)
        self.assertIsInstance(flipped_image, Image.Image)

    def test_change_brightness(self):
        """
        Test changing the brightness of an image.
        """
        bright_image = change_brightness(self.image, factor=1.5)
        self.assertIsNotNone(bright_image)
        self.assertIsInstance(bright_image, Image.Image)

    def test_change_contrast(self):
        """
        Test changing the contrast of an image.
        """
        contrast_image = change_contrast(self.image, factor=1.5)
        self.assertIsNotNone(contrast_image)
        self.assertIsInstance(contrast_image, Image.Image)

    def test_add_noise(self):
        """
        Test adding noise to an image.
        """
        noisy_image = add_noise(self.image, amount=0.1)
        self.assertIsNotNone(noisy_image)
        self.assertIsInstance(noisy_image, Image.Image)

    def test_shift_image(self):
        """
        Test shifting an image.
        """
        shifted_image = shift_image(self.image, shift=(10, 10))
        self.assertIsNotNone(shifted_image)
        self.assertIsInstance(shifted_image, Image.Image)

    def test_random_crop(self):
        """
        Test performing a random crop on an image.
        """
        cropped_image = random_crop(self.image, size=(50, 50))
        self.assertIsNotNone(cropped_image)
        self.assertEqual(cropped_image.size, (50, 50))

    def test_overlay_text(self):
        """
        Test overlaying text on an image.
        """
        text_image = overlay_text(self.image, text="Test", position=(10, 10))
        self.assertIsNotNone(text_image)
        self.assertIsInstance(text_image, Image.Image)

    def test_overlay_image(self):
        """
        Test overlaying an image on another image.
        """
        overlay = Image.new('RGB', (50, 50), color='blue')
        overlayed_image = overlay_image(
            self.image,
            overlay=overlay,
            position=(25, 25),
            transparency=0.5
        )
        self.assertIsNotNone(overlayed_image)
        self.assertIsInstance(overlayed_image, Image.Image)


if __name__ == '__main__':
    unittest.main()
