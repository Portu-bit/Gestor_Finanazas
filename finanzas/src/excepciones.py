#ecxepciones personalizadas, monto negativo, saldo insuficiente y tipo de transaccion no valida  
class MontoNegativoError(Exception):
    pass

class SaldoInsuficienteError(Exception):
    pass

class TipoTransaccionInvalidaError(Exception):
    pass