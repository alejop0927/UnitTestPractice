import pytest

from src.model.tarjetadecredito import TarjetaDeCredito
from src.model.compra import Compra

def test_caso_36_cuotas():
    tarjeta_de_credito: TarjetaDeCredito = TarjetaDeCredito(3.1, 1000000)
    # Change from Compra[...] to Compra(...)
    compra: Compra = Compra(200000, 3.1, 36)
    tarjeta_de_credito.registrer_compra(compra)
    total_interes = tarjeta_de_credito.calcular_total_interes()
    assert total_interes == 134726.53


def test_caso_24_cuotas():
    tarjeta_de_credito: TarjetaDeCredito = TarjetaDeCredito(3.1, 1000000)
    # Change from Compra[...] to Compra(...)
    compra: Compra = Compra(850000, 3.4, 24)
    tarjeta_de_credito.registrer_compra(compra)
    total_interes = tarjeta_de_credito.calcular_total_interes()
    assert total_interes == 407059.97

def test_caso_48_cuotas():
    tarjeta_de_credito: TarjetaDeCredito = TarjetaDeCredito(3.1, 1000000)
    # Change from Compra[...] to Compra(...)
    compra: Compra = Compra(48000,0 , 48)
    tarjeta_de_credito.registrer_compra(compra)
    total_interes = tarjeta_de_credito.calcular_total_interes()
    assert total_interes == 0

def test_caso_60_cuotas():
    tarjeta_de_credito: TarjetaDeCredito = TarjetaDeCredito(3.1, 1000000)
    # Change from Compra[...] to Compra(...)
    compra: Compra = Compra(5000, 12.5, 60)
    tarjeta_de_credito.registrer_compra(compra)
    total_interes = tarjeta_de_credito.calcular_total_interes()
    assert total_interes == 'La tasa de interés supera la tasa de usura'

def test_caso_1_cuotas():
    tarjeta_de_credito: TarjetaDeCredito = TarjetaDeCredito(3.1, 1000000)
    # Change from Compra[...] to Compra(...)
    compra: Compra = Compra(9000, 2.4, 1)
    tarjeta_de_credito.registrer_compra(compra)
    total_interes = tarjeta_de_credito.calcular_total_interes()
    assert total_interes == 0

def test_caso_60_cuotas():
    tarjeta_de_credito: TarjetaDeCredito = TarjetaDeCredito(3.1, 1000000)
    # Change from Compra[...] to Compra(...)
    compra: Compra = Compra(0, 2.4, 60)
    tarjeta_de_credito.registrer_compra(compra)
    total_interes = tarjeta_de_credito.calcular_total_interes()
    assert total_interes == ' el monto debe ser superior a cero'

def test_caso_10_cuotas():
    tarjeta_de_credito: TarjetaDeCredito = TarjetaDeCredito(3.1, 1000000)
    # Change from Compra[...] to Compra(...)
    compra: Compra = Compra(50000, 1, -10)
    tarjeta_de_credito.registrer_compra(compra)
    total_interes = tarjeta_de_credito.calcular_total_interes()
    assert total_interes == 'el número de cuotas debe ser mayor a cero'
