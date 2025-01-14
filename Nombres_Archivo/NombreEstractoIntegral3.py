import os
import shutil
import re

# Diccionario para convertir nombres de meses a números
meses = {
    "Enero": "01", "Febrero": "02", "Marzo": "03", "Abril": "04", 
    "Mayo": "05", "Junio": "06", "Julio": "07", "Agosto": "08",
    "Septiembre": "09", "Octubre": "10", "Noviembre": "11", "Diciembre": "12"
}

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
    patron = r"^Resumen \d{2} \d{2} ([A-Za-z]+) (\d{4})\.pdf$"

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
            mes_texto, anio = coincidencia.groups()
            print(f" -> Coincidencia encontrada: Mes: {mes_texto}, Año: {anio}")
            mes_numero = meses.get(mes_texto)
            
            # Si el mes no es válido, ignorar el archivo
            if not mes_numero:
                print(f" -> Mes no válido: {mes_texto}")
                continue
            
            # Construir el nuevo nombre del archivo
            nuevo_nombre = f"{anio} {mes_numero} Extracto Integral Enrique.pdf"
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
