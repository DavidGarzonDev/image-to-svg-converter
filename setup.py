from setuptools import setup, find_packages

setup(
    name="converter-svg",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "Pillow",
        "svgwrite"
    ],
    entry_points={
        "console_scripts": [
            "converter-svg=app.cli:main",  # Comando que se ejecutará y función principal
        ],
    },
    author="Tu Nombre",
    description="Una herramienta para convertir imágenes a SVG.",
    python_requires=">=3.7",
)
