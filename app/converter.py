from PIL import Image
import svgwrite
import os

def image_to_svg(input_image_path, output_svg_path, scale=1):
    """
    Convierte una imagen a SVG con reducción de resolución.
    :param input_image_path: Ruta de la imagen de entrada.
    :param output_svg_path: Ruta del archivo SVG de salida.
    :param scale: Factor de escala para reducir la resolución (0.5 = 50% del tamaño original).
    """
    # Abrir la imagen usando Pillow
    img = Image.open(input_image_path)
    img = img.convert("RGBA")  # Convertir a RGBA para manejar transparencias

    # Reducir el tamaño de la imagen
    width, height = img.size
    new_width = max(1, int(width * scale))  # Asegurarse de que no sea menor que 1 píxel
    new_height = max(1, int(height * scale))
    img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

    # Crear un archivo SVG
    dwg = svgwrite.Drawing(output_svg_path, size=(new_width, new_height))
    # Obtener los píxeles de la imagen redimensionada
    pixels = img.load()

    # Crear un rectángulo por cada píxel
    for x in range(new_width):
        for y in range(new_height):
            r, g, b, a = pixels[x, y]  # Incluye el canal alfa (transparencia)
            if a > 0:  # Solo agrega píxeles visibles
                dwg.add(dwg.rect(insert=(x, y), size=(1, 1), fill=svgwrite.rgb(r, g, b, '%')))

    dwg.save()
    print(f"SVG generado")

def convert_images_in_folder(input_folder, output_folder, scale=0.5):
    """
    Convierte todas las imágenes de una carpeta a formato SVG.
    :param input_folder: Carpeta de entrada con imágenes.
    :param output_folder: Carpeta de salida para los archivos SVG.
    :param scale: Factor de escala para reducir la resolución.
    """
    # Crear la carpeta de salida si no existe
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Recorrer todos los archivos en la carpeta de entrada
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)

        # Filtrar solo las imágenes (puedes agregar más extensiones si es necesario)
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            output_svg_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.svg")
            image_to_svg(input_path, output_svg_path, scale=scale)
