import argparse
import os
from app.converter import convert_images_in_folder

def main():
    parser = argparse.ArgumentParser(description='Convert images to SVG format')
    parser.add_argument('input_folder', type=str, help='Path to the folder with images')
    parser.add_argument('output_folder', type=str, help='Path to the folder to save SVG files')

    args = parser.parse_args()

    # Verificar si las carpetas existen
    if not os.path.exists(args.input_folder):
        print(f"Error: La carpeta de entrada {args.input_folder} no existe.")
        return

    if not os.path.exists(args.output_folder):
        os.makedirs(args.output_folder)

    # Llamar a la función para convertir las imágenes
    convert_images_in_folder(args.input_folder, args.output_folder)
    print(f"Conversión completa. Las imágenes SVG se han guardado en {args.output_folder}")

if __name__ == "__main__":
    main()
