

import pytest

from projeto.carteira_digital import CarteiraDigital
from projeto.exceptions.saldo_insuficiente import SaldoInsuficienteError



def test_iniciar_carteira():
    # Arrange
    valor_inicial = 400
    # Act 
    carteira = CarteiraDigital(valor_inicial)
    # Assert
    assert carteira.saldo == valor_inicial

def test_depositar_100(carteira:CarteiraDigital):
    # Arrange
    valor_a_ser_depositado = 100
    #  # Act
    
    carteira.depositar(valor=valor_a_ser_depositado)
    
    
    # Assert

    assert carteira.saldo == 1100

def test_sacar_1000(carteira:CarteiraDigital):
    # Arrange
    valor_a_ser_sacado = 1000
    # Act
    carteira.sacar(valor=valor_a_ser_sacado)
    # Assert
    assert carteira.saldo ==0


def test_sacar_900(carteira:CarteiraDigital):
    # Arrange
    valor_a_ser_sacado = 900
    # Act
    carteira.sacar(valor=valor_a_ser_sacado)
    # Assert
    assert carteira.saldo ==100


def test_sacar_valor_acima_saldo(carteira:CarteiraDigital):
    # Arrange
    valor_a_ser_sacado = 1200
    # Act & assert
    
    with pytest.raises(SaldoInsuficienteError):
        carteira.sacar(valor=valor_a_ser_sacado)


def test_sacar_valor_acima_saldo_e_saldo_nao_muda(carteira: CarteiraDigital):
    # Arrange
    valor_a_ser_sacado = 1200
    # Act & assert
    
    with pytest.raises(SaldoInsuficienteError):
        carteira.sacar(valor=valor_a_ser_sacado)
    
    # Assert
    assert carteira.saldo == 1000