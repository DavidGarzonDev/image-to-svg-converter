from PIL import Image
import svgwrite
import os

def image_to_svg(input_image_path, output_svg_path, scale=1):
    """
    Converts an image to SVG with resolution reduction.
    :param input_image_path: Input image path.
    :param output_svg_path: Path to the output SVG file.
    :param scale: Scaling factor to reduce resolution (0.5 = 50% of original size).
    """
    # Open image using Pillow
    img = Image.open(input_image_path)
    img = img.convert("RGBA")  # Convert to RGBA to handle transparencies

    # Reduce image size
    width, height = img.size
    new_width = max(1, int(width * scale))  # Make sure it is no smaller than 1 pixel.
    new_height = max(1, int(height * scale))
    img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

    # Create an SVG file
    dwg = svgwrite.Drawing(output_svg_path, size=(new_width, new_height))
    # Get pixels of the resized image
    pixels = img.load()

    # Create a rectangle for each pixel
    for x in range(new_width):
        for y in range(new_height):
            r, g, b, a = pixels[x, y]  # Includes alpha channel (transparency)
            if a > 0:  # Only adds visible pixels
                dwg.add(dwg.rect(insert=(x, y), size=(1, 1), fill=svgwrite.rgb(r, g, b, '%')))

    dwg.save()
    print(f"SVG generated")

def convert_images_in_folder(input_folder, output_folder, scale=0.5):
    """
    Converts all images in a folder to SVG format.
    :param input_folder: Input folder with images.
    :param output_folder: Output folder for SVG files.
    :param scale: Scale factor to reduce resolution.
    """
    # Create the output folder if it does not exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Scroll through all files in the input folder
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)

        #  Filter only images (you can add more extensions if needed)
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            output_svg_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.svg")
            image_to_svg(input_path, output_svg_path, scale=scale)
