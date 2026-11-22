import sqlite3
from datetime import datetime


def crear_tabla_transacciones(db='finanzas.db'):
    """Create the transactions table without deleting existing records."""
    with sqlite3.connect(db) as conn:
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


def insertar_transaccion(tipo, descripcion, monto, db='finanzas.db'):
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with sqlite3.connect(db) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO transacciones (fecha, tipo, monto, descripcion)
            VALUES (?, ?, ?, ?)
        ''', (fecha, tipo, monto, descripcion))


def obtener_transacciones(db='finanzas.db'):
    with sqlite3.connect(db) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM transacciones ORDER BY id')
        return cursor.fetchall()
