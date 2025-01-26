import argparse
import os
from app.converter import convert_images_in_folder

def main():
    parser = argparse.ArgumentParser(description='Convert images to SVG format')
    parser.add_argument('input_folder', type=str, help='Path to the folder with images')
    parser.add_argument('output_folder', type=str, help='Path to the folder to save SVG files')

    args = parser.parse_args()

    # Check if the folders exist
    if not os.path.exists(args.input_folder):
        print(f" Error: The input folder{args.input_folder} does not exist.")
        return

    if not os.path.exists(args.output_folder):
        os.makedirs(args.output_folder)

    # Calling the function to convert images
    convert_images_in_folder(args.input_folder, args.output_folder)
    print(f"Conversion complete. SVG images have been saved in {args.output_folder}")

if __name__ == "__main__":
    main()
