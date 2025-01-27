# Converter-SVG

Converter-SVG es una herramienta ligera para convertir imágenes en formato SVG, optimizando su peso para que sean más manejables en proyectos web o de diseño.

## Características
- Convierte imágenes de carpetas completas a formato SVG.
- Reduce el tamaño de las imágenes para optimizar su uso.
- Compatible con sistemas Windows, Linux y macOS.
- Personalizable mediante opciones de entrada y salida.

---

## Requisitos
- Python 3.9 o superior.
- Entorno virtual configurado (recomendado).

### Dependencias
Este proyecto utiliza las siguientes librerías:
- `Pillow`: Para manipular y procesar imágenes.
- `svgwrite`: Para generar archivos SVG.
- `pytest`: Para pruebas automatizadas.
- `setuptools`: Para empaquetar el proyecto.


---

## Instalación
1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/tu-usuario/converter-svg.git
   cd converter-svg
   ```

2. **Configura un entorno virtual**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/MacOS
   venv\Scripts\activate   # Windows
   ```

3. **Instala las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Instala el paquete**:
   ```bash
   pip install .
   ```

---

## Uso
Una vez instalado, puedes usar el comando `converter-svg` para convertir tus imágenes.

### Ejemplo de uso
```bash
converter-svg carpeta-de-entrada carpeta-de-salida
```
- **`carpeta-de-entrada`**: Carpeta que contiene las imágenes a convertir.
- **`carpeta-de-salida`**: Carpeta donde se guardarán los archivos SVG generados.

Si las carpetas no existen, el programa las creará automáticamente.

---

## Pruebas
Para ejecutar las pruebas, asegúrate de que `pytest` esté instalado y ejecuta:
```bash
pytest
```
Esto validará que todas las funcionalidades del proyecto están funcionando correctamente.

---

## Contribuciones
¡Las contribuciones son bienvenidas! Por favor, sigue estos pasos:
1. Realiza un fork del repositorio.
2. Crea una nueva rama con un nombre descriptivo de tu cambio.
   ```bash
   git checkout -b feat-nueva-funcionalidad
   ```
3. Realiza tus cambios y realiza un commit.
   ```bash
   git commit -m "feat: descripción breve de la funcionalidad"
   ```
4. Envía un pull request explicando tus cambios.

---

## Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.

