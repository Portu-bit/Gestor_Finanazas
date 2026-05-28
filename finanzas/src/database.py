# crear una funcion que cree la tabla "transacciopnes" en la base de datos "finanzas.db" con los siguientes campos: id, fecha, tipo, monto y descripcion
import sqlite3
from datetime import datetime

def crear_tabla_transacciones():
    with sqlite3.connect('finanzas.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS transacciones (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fecha TEXT NOT NULL,
                tipo TEXT NOT NULL,
                monto REAL NOT NULL,
                descripcion TEXT
            )
        ''')

def insertar_transaccion(tipo, descripcion, monto):
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with sqlite3.connect('finanzas.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO transacciones (fecha, tipo, monto, descripcion)
            VALUES (?, ?, ?, ?)
        ''', (fecha, tipo, monto, descripcion))

def obtener_transacciones():
    with sqlite3.connect('finanzas.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM transacciones')
        transacciones = cursor.fetchall()
    return transacciones