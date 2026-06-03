#exportar las transacciones a un archivo csv, con el formato fecha, tipo, monto, categoria y descripcion
import csv
from src.database import obtener_transacciones

def exportar_csv(nombre_archivo):
    transacciones = obtener_transacciones()
    with open(nombre_archivo, mode='w', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow(['ID', 'Fecha', 'Tipo', 'Monto', 'Descripcion'])
        for transaccion in transacciones:
            escritor_csv.writerow(transaccion)