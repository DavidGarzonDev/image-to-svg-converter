import os
import pytest
from PIL import Image
from app.converter import convert_images_in_folder

# Fixture de pytest para crear un directorio temporal
@pytest.fixture
def setup_directories(tmpdir):
    # Crear carpeta de entrada
    input_folder = tmpdir.mkdir("test_input")
    output_folder = tmpdir.mkdir("test_output")

    # Crear una imagen de prueba válida con Pillow
    test_image_path = input_folder.join("test_image.png")
    image = Image.new("RGB", (100, 100), color=(255, 0, 0))  # Crear una imagen roja
    image.save(str(test_image_path))

    return input_folder, output_folder

def test_image_to_svg_conversion(setup_directories):
    input_folder, output_folder = setup_directories

    # Ejecutar la función de conversión
    convert_images_in_folder(str(input_folder), str(output_folder))

    # Verificar que el archivo SVG se haya creado
    output_svg_path = os.path.join(str(output_folder), "test_image.svg")
    assert os.path.exists(output_svg_path), f"El archivo SVG no se ha creado en {output_svg_path}"

def test_output_folder_creation(setup_directories):
    input_folder, output_folder = setup_directories

    # Asegurarse de que la carpeta de salida existe
    assert os.path.exists(str(output_folder)), f"La carpeta de salida {output_folder} no existe"

    # Ejecutar la función de conversión
    convert_images_in_folder(str(input_folder), str(output_folder))

    # Verificar que el archivo SVG se ha creado
    output_svg_path = os.path.join(str(output_folder), "test_image.svg")
    assert os.path.exists(output_svg_path), f"El archivo SVG no se ha creado en {output_svg_path}"
