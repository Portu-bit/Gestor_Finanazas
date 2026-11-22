import csv

from .database import obtener_transacciones


def exportar_csv(nombre_archivo, db='finanzas.db'):
    """Export transactions from the selected database to a CSV file."""
    transacciones = obtener_transacciones(db=db)

    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow(
            ['ID', 'Fecha', 'Tipo', 'Monto', 'Descripcion']
        )
        escritor_csv.writerows(transacciones)
