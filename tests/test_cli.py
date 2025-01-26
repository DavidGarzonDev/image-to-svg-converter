import unittest
import os
import shutil
from PIL import Image
from app.converter import convert_images_in_folder

class TestImageConversion(unittest.TestCase):

    def setUp(self):
        #  It is executed before each test. Temporary folders are created.
        self.input_folder = 'test_input'
        self.output_folder = 'test_output'

        # Create an input folder with a valid test image
        os.makedirs(self.input_folder, exist_ok=True)

        # Create a valid test PNG image using Pillow
        img = Image.new('RGB', (100, 100), color=(73, 109, 137))  # An image of 100x100 pixels
        img.save(os.path.join(self.input_folder, 'test_image.png'))

    def tearDown(self):
        # Run after each test. Clean the created folders.
        if os.path.exists(self.input_folder):
            shutil.rmtree(self.input_folder)
        if os.path.exists(self.output_folder):
            shutil.rmtree(self.output_folder)

    def test_image_conversion(self):
        # We call the function we want to test
        convert_images_in_folder(self.input_folder, self.output_folder)

        # Verify that the SVG file has been created in the output folder
        output_file = os.path.join(self.output_folder, 'test_image.svg')
        self.assertTrue(os.path.exists(output_file), "El archivo SVG no se ha creado.")

    def test_output_folder_creation(self):
        # Verify that the output folder is created if it does not exist
        if os.path.exists(self.output_folder):
            shutil.rmtree(self.output_folder)
        
        convert_images_in_folder(self.input_folder, self.output_folder)
        self.assertTrue(os.path.exists(self.output_folder), "The output folder has not been created.")

    def test_no_input_folder(self):
        # Verify that the case where the input folder does not exist is handled correctly.
        non_existent_folder = 'non_existent_folder'
        with self.assertRaises(FileNotFoundError):
            convert_images_in_folder(non_existent_folder, self.output_folder)

if __name__ == '__main__':
    unittest.main()
