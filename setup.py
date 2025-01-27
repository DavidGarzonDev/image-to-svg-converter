from setuptools import setup, find_packages

setup(
    name="converter-svg",
    version="1.0.1",
    packages=find_packages(),
    install_requires=[
        "Pillow",
        "svgwrite",
        "pytest",
    ],
    entry_points={
        "console_scripts": [
            "converter-svg=app.cli:main",  # Command to be executed and main function
        ],
    },
    author="Juan David Garzon",
    description="A tool to convert images to SVG.",
    python_requires=">=3.7",
)
