import os
import pytest
from PIL import Image
from app.converter import convert_images_in_folder

# Fixture of pytest to create a temporary directory
@pytest.fixture
def setup_directories(tmpdir):
    # Create input folder
    input_folder = tmpdir.mkdir("test_input")
    output_folder = tmpdir.mkdir("test_output")

    # Create a valid test image with Pillow
    test_image_path = input_folder.join("test_image.png")
    image = Image.new("RGB", (100, 100), color=(255, 0, 0))  # Create a red image
    image.save(str(test_image_path))

    return input_folder, output_folder

def test_image_to_svg_conversion(setup_directories):
    input_folder, output_folder = setup_directories

    # Execute the conversion function
    convert_images_in_folder(str(input_folder), str(output_folder))

    # Verify that the SVG file has been created
    output_svg_path = os.path.join(str(output_folder), "test_image.svg")
    assert os.path.exists(output_svg_path), f"SVG file has not been created in{output_svg_path}"

def test_output_folder_creation(setup_directories):
    input_folder, output_folder = setup_directories

    #  Make sure that the output folder exists.
    assert os.path.exists(str(output_folder)), f"The output folder {output_folder} does not exist"

    # Execute the conversion function
    convert_images_in_folder(str(input_folder), str(output_folder))

    # Verify that the SVG file has been created
    output_svg_path = os.path.join(str(output_folder), "test_image.svg")
    assert os.path.exists(output_svg_path), f"SVG file has not been created in {output_svg_path}"
