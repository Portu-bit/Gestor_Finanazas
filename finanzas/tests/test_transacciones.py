import pytest
import os 
import sqlite3
from src.transacciones import GestorFinanzas
from src.database import crear_tabla_transacciones

@pytest.fixture
def gestor():
    # Crear un gestor de finanzas con una base de datos de prueba
    crear_tabla_transacciones(db='test_finanzas.db')
    gestor = GestorFinanzas(db='test_finanzas.db')
    yield gestor
    # Limpiar la base de datos después de cada prueba
    # Cerrar cualquier conexión abierta a la BD
    try:
        conn = sqlite3.connect('test_finanzas.db')
        conn.close()
    except:
        pass
    if os.path.exists('test_finanzas.db'):
        try:
            os.remove('test_finanzas.db')
        except:
            pass

def test_agregar_ingreso(gestor):
    gestor.agregar_ingreso(1000, "Salario")
    transacciones = gestor.obtener_transacciones()
    assert len(transacciones) == 1
    assert transacciones[0][2] == "ingreso"
    assert transacciones[0][3] == 1000
    assert transacciones[0][4] == "Salario"

def test_agregar_gasto(gestor):
    gestor.agregar_ingreso(1000, "Salario")
    gestor.agregar_gasto(200, "Comida")
    transacciones = gestor.obtener_transacciones()
    assert len(transacciones) == 2
    assert transacciones[1][2] == "gasto"
    assert transacciones[1][3] == 200
    assert transacciones[1][4] == "Comida"

def test_saldo_insuficiente(gestor):
    gestor.agregar_ingreso(500, "Salario")
    with pytest.raises(Exception) as excinfo:
        gestor.agregar_gasto(600, "Renta")
    assert "Saldo insuficiente" in str(excinfo.value)

def test_monto_invalido(gestor):
    with pytest.raises(Exception) as excinfo:
        gestor.agregar_ingreso(-100, "Salario")
    assert "El monto no puede ser negativo" in str(excinfo.value)