class TarjetaDeCredito:
    def __init__(self, cupo_disponible:float,tasa_interes:float):
        self.cupo_disponible=cupo_disponible
        self.tasa_interes=tasa_interes
    

class Compra(TarjetaDeCredito):
    def __init__(self, cupo_disponible, tasa_interes,monto:float,numero_cupos:int):
        self.monto=monto
        self.numero_cupos=numero_cupos
        super().__init__(cupo_disponible, tasa_interes)

class planamortizacion(Compra):      
    def __init__(self, cupo_disponible, tasa_interes, numero_de_cuotas:int, saldo_pendiente: float, cuota_mensual: float, interes_mensual: float):
        self.numero_de_cuotas=numero_de_cuotas
        self.saldo_pendiente=saldo_pendiente
        self.cuota_mensual=cuota_mensual
        self.interes_mensual=interes_mensual
        super().__init__(cupo_disponible, tasa_interes)

class cuotamensual(planamortizacion):
    def __init__(self, cupo_disponible, tasa_interes, numero_de_cuotas, saldo_pendiente, cuota_mensual, interes_mensual,pago_capital:float,pago_interes:float,id_cuota:int,valor_cuota:float):
        self.pago_capital=pago_capital
        self.pago_interes=pago_interes
        self.id_cuota=id_cuota
        self.valor_cuota=valor_cuota
        super().__init__(cupo_disponible, tasa_interes, numero_de_cuotas, saldo_pendiente, cuota_mensual, interes_mensual)