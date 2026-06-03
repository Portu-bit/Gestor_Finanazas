
from src.excepciones import MontoNegativoError, TipoTransaccionInvalidaError, SaldoInsuficienteError
from src.database import insertar_transaccion, obtener_transacciones


class GestorFinanzas:
    def __init__(self, db='finanzas.db'):
        self.db = db

    def agregar_ingreso(self, monto, descripcion):
        if monto <= 0:
            raise MontoNegativoError("El monto no puede ser negativo.")
        
        if not descripcion:
            raise TipoTransaccionInvalidaError("La descripción no puede estar vacía.")
        
        insertar_transaccion(tipo="ingreso", descripcion=descripcion, monto=monto, db=self.db)

    def agregar_gasto(self, monto, descripcion):
        if monto <= 0:
            raise MontoNegativoError("El monto no puede ser negativo.")
        
        if monto > self.obtener_balance():
            raise SaldoInsuficienteError("Saldo insuficiente para realizar esta transacción.")
        
        if not descripcion:
            raise TipoTransaccionInvalidaError("La descripción no puede estar vacía.")
        
        insertar_transaccion(tipo="gasto", descripcion=descripcion, monto=monto, db=self.db)
    
    #una funcion que suma ingresos, resta gastos, retorna el resultado
    def obtener_balance(self):
        transacciones = obtener_transacciones(db=self.db)
        balance = 0.0
        for transaccion in transacciones:
            if transaccion[2] == "ingreso":
                balance += transaccion[3]
            elif transaccion[2] == "gasto":
                balance -= transaccion[3]
        return balance
    
    def obtener_transacciones(self):
        return obtener_transacciones(db=self.db)