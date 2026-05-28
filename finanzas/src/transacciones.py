
from finanzas.src.excepciones import MontoNegativoError, TipoTransaccionInvalidaError, SaldoInsuficienteError
from finanzas.src.database import insertar_transaccion, obtener_transacciones


class GestorFinanzas:
    def __init__(self):
        pass

    def agregar_ingreso(self, monto, descripcion):
        if monto <= 0:
            raise MontoNegativoError("El monto no puede ser negativo.")
        
        if not descripcion:
            raise TipoTransaccionInvalidaError("La descripción no puede estar vacía.")
        
        insertar_transaccion("ingreso", descripcion, monto)

    def agregar_gasto(self, monto, descripcion):
        if monto <= 0:
            raise MontoNegativoError("El monto no puede ser negativo.")
        
        if monto > self.obtener_balance():
            raise SaldoInsuficienteError("Saldo insuficiente para realizar esta transacción.")
        
        if not descripcion:
            raise TipoTransaccionInvalidaError("La descripción no puede estar vacía.")
        
        insertar_transaccion("gasto", descripcion, monto)
    
    #una funcion que suma ingresos, resta gastos, retorna el resultado
    def obtener_balance(self):
        transacciones = obtener_transacciones()
        balance = 0.0
        for transaccion in transacciones:
            if transaccion[2] == "ingreso":
                balance += transaccion[3]
            elif transaccion[2] == "gasto":
                balance -= transaccion[3]
        return balance
    
    def obtener_transacciones(self):
        return obtener_transacciones()