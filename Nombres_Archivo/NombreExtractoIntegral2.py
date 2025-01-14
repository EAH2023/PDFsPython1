import os
import shutil
import re

def procesar_archivos():
    # Solicitar rutas de origen y destino
    origen = input("Introduce la ruta de la carpeta de origen: ").strip()
    destino = input("Introduce la ruta de la carpeta de destino: ").strip()

    # Validar si las rutas existen
    if not os.path.isdir(origen):
        print("La carpeta de origen no existe.")
        return
    if not os.path.isdir(destino):
        print("La carpeta de destino no existe.")
        return

    # Expresión regular para validar y extraer información del nombre del archivo
    patron = r"^Resumen (\d{4}) (\d{1,2}).*\.pdf$"

    print("\nArchivos en la carpeta de origen:")
    for archivo in os.listdir(origen):
        print(f" - {archivo}")

    print("\nProcesando archivos...\n")

    # Procesar archivos en la carpeta de origen
    for archivo in os.listdir(origen):
        ruta_archivo = os.path.join(origen, archivo)

        # Saltar si no es un archivo
        if not os.path.isfile(ruta_archivo):
            print(f"IGNORADO (no es un archivo): {archivo}")
            continue

        # Intentar encontrar el patrón en el nombre del archivo
        print(f"Comprobando archivo: {archivo}")
        coincidencia = re.match(patron, archivo)
        if coincidencia:
            anio, mes = coincidencia.groups()
            print(f" -> Coincidencia encontrada: Año: {anio}, Mes: {mes}")

            # Asegurar que el mes tenga dos dígitos
            mes_dos_digitos = mes.zfill(2)

            # Construir el nuevo nombre del archivo
            nuevo_nombre = f"{anio} {mes_dos_digitos} Extracto Integral Enrique.pdf"
            ruta_destino = os.path.join(destino, nuevo_nombre)

            # Copiar el archivo con el nuevo nombre
            shutil.copy(ruta_archivo, ruta_destino)
            print(f" -> Copiado: {archivo} -> {nuevo_nombre}")
        else:
            print(f" -> NO coincide con el patrón: {archivo}")

    print("\n¡Procesamiento completo!")

# Ejecutar la función
if __name__ == "__main__":
    procesar_archivos()
