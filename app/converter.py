from PIL import Image
import svgwrite
import os

def open_and_resize_image(image_path, scale):
    """
    Opens and resizes an image according to the scale factor.
    :param image_path: Path to the input image.
    :param scale: Scale factor to reduce resolution.
    :return: Resized image and its dimensions.
    """
    img = Image.open(image_path).convert("RGBA")
    width, height = img.size
    new_width = max(1, int(width * scale))
    new_height = max(1, int(height * scale))
    img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
    return img, new_width, new_height

def generate_svg(img, output_svg_path, width, height):
    """
    Generates an SVG file from a resized image.
    :param img: Resized image.
    :param output_svg_path: Path to the output SVG file.
    :param width: Image width.
    :param height: Image height.
    """
    dwg = svgwrite.Drawing(output_svg_path, size=(width, height))
    pixels = img.load()

    for x in range(width):
        for y in range(height):
            r, g, b, a = pixels[x, y]
            if a > 0:
                dwg.add(dwg.rect(insert=(x, y), size=(1, 1), fill=svgwrite.rgb(r, g, b, '%')))
    
    dwg.save()
    print(f"SVG generated: {output_svg_path}")

def image_to_svg(input_image_path, output_svg_path, scale=1):
    """
    Converts an image to SVG format with resolution reduction.
    """
    img, new_width, new_height = open_and_resize_image(input_image_path, scale)
    generate_svg(img, output_svg_path, new_width, new_height)

def convert_images_in_folder(input_folder, output_folder, scale=0.5):
    """
    Converts all images in a folder to SVG format.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(input_folder, filename)
            output_svg_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.svg")
            image_to_svg(input_path, output_svg_path, scale)