# Convertir Imágenes a WebP

Este script convierte imágenes en formato PNG, JPG y JPEG a formato WebP utilizando la biblioteca `Pillow` (PIL) en Python. Puedes usarlo para optimizar imágenes y reducir su tamaño sin perder calidad.

## Descripción

Este script recorre todos los archivos en una carpeta de entrada especificada, verifica si los archivos son imágenes en formato PNG, JPG o JPEG, y luego los convierte al formato WebP. Las imágenes convertidas se guardan en una carpeta de salida.

### Características

- Convierte imágenes de los formatos `.png`, `.jpg`, y `.jpeg` a `.webp`.
- Crea una carpeta de salida si no existe.
- Permite ajustar la calidad de las imágenes convertidas (con un valor predeterminado de calidad al 90%).
- Imprime en la consola los nombres de los archivos convertidos.

## Requisitos

- Python 3.x
- Biblioteca Pillow (PIL)

Para instalar Pillow, usa el siguiente comando:

```bash
pip install Pillow
