import os
from PIL import Image

def convertir_imagenes_a_webp(carpetaEntrada, carpetaSalida):
    # Comprobamos si la carpeta de salida existe, si no, la creamos
    if not os.path.exists(carpetaSalida):
        os.makedirs(carpetaSalida)

    # Recorremos todos los archivos en la carpeta de entrada
    for archivo in os.listdir(carpetaEntrada):
        # Comprobamos si es un archivo de imagen PNG o JPG
        if archivo.endswith(".png") or archivo.endswith(".jpg") or archivo.endswith(".jpeg"):
            # Obtenemos la ruta completa del archivo de entrada
            rutaEntrada = os.path.join(carpetaEntrada, archivo)

            # Abrimos la imagen
            imagen = Image.open(rutaEntrada)

            # Convertimos y guardamos la imagen en formato WebP en la carpeta de salida
            nombreSalida = os.path.splitext(archivo)[0] + ".webp"
            rutaSalida = os.path.join(carpetaSalida, nombreSalida)
            imagen.save(rutaSalida, "WEBP", quality=90)  # Puedes ajustar la calidad según necesites

            print(f"Convertido {archivo} a {nombreSalida}")

# Rutas de la carpeta de entrada y la carpeta de salida
carpetaEntrada = "./img-entrada"
carpetaSalida = "./img-salida"

# Llamar a la función para convertir las imágenes
convertir_imagenes_a_webp(carpetaEntrada, carpetaSalida)