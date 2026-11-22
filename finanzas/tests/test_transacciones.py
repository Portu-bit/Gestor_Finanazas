import pytest

from finanzas.src.database import crear_tabla_transacciones
from finanzas.src.excepciones import (
    MontoNegativoError,
    SaldoInsuficienteError,
    TipoTransaccionInvalidaError,
)
from finanzas.src.transacciones import GestorFinanzas


@pytest.fixture
def gestor(tmp_path):
    db_path = tmp_path / "test_finanzas.db"
    crear_tabla_transacciones(db=str(db_path))
    return GestorFinanzas(db=str(db_path))


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


def test_no_perder_datos_al_crear_tabla_de_nuevo(gestor):
    gestor.agregar_ingreso(1000, "Salario")

    crear_tabla_transacciones(db=gestor.db)

    transacciones = gestor.obtener_transacciones()

    assert len(transacciones) == 1
    assert transacciones[0][4] == "Salario"


def test_saldo_insuficiente(gestor):
    gestor.agregar_ingreso(500, "Salario")

    with pytest.raises(SaldoInsuficienteError):
        gestor.agregar_gasto(600, "Renta")


@pytest.mark.parametrize("monto", [-100, 0])
def test_monto_invalido(gestor, monto):
    with pytest.raises(MontoNegativoError):
        gestor.agregar_ingreso(monto, "Salario")


def test_descripcion_vacia(gestor):
    with pytest.raises(TipoTransaccionInvalidaError):
        gestor.agregar_ingreso(100, "   ")
