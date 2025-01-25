import unittest
import os
import shutil
from PIL import Image
from app.converter import convert_images_in_folder

class TestImageConversion(unittest.TestCase):

    def setUp(self):
        # Se ejecuta antes de cada prueba. Se crean carpetas temporales.
        self.input_folder = 'test_input'
        self.output_folder = 'test_output'

        # Crear una carpeta de entrada con una imagen de prueba válida
        os.makedirs(self.input_folder, exist_ok=True)

        # Crear una imagen PNG válida de prueba usando Pillow
        img = Image.new('RGB', (100, 100), color=(73, 109, 137))  # Una imagen de 100x100 píxeles
        img.save(os.path.join(self.input_folder, 'test_image.png'))

    def tearDown(self):
        # Se ejecuta después de cada prueba. Limpiar las carpetas creadas.
        if os.path.exists(self.input_folder):
            shutil.rmtree(self.input_folder)
        if os.path.exists(self.output_folder):
            shutil.rmtree(self.output_folder)

    def test_image_conversion(self):
        # Llamamos a la función que queremos probar
        convert_images_in_folder(self.input_folder, self.output_folder)

        # Verificar que el archivo SVG se haya creado en la carpeta de salida
        output_file = os.path.join(self.output_folder, 'test_image.svg')
        self.assertTrue(os.path.exists(output_file), "El archivo SVG no se ha creado.")

    def test_output_folder_creation(self):
        # Verificar que la carpeta de salida se crea si no existe
        if os.path.exists(self.output_folder):
            shutil.rmtree(self.output_folder)
        
        convert_images_in_folder(self.input_folder, self.output_folder)
        self.assertTrue(os.path.exists(self.output_folder), "La carpeta de salida no se ha creado.")

    def test_no_input_folder(self):
        # Verificar que se maneje correctamente el caso de que la carpeta de entrada no existe
        non_existent_folder = 'non_existent_folder'
        with self.assertRaises(FileNotFoundError):
            convert_images_in_folder(non_existent_folder, self.output_folder)

if __name__ == '__main__':
    unittest.main()
