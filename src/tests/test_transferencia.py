from projeto.exceptions.saldo_insuficiente import SaldoInsuficienteError
from projeto.transferencia import transferir
import pytest

@pytest.mark.parametrize("valor",[100,200,300])
def test_transferir(carteiras,valor):
    carteira_1,carteira_destino = carteiras

    transferir(carteira_1,carteira_destino,valor)

    assert carteira_destino.saldo == valor
    assert carteira_1.saldo == 1000 - valor


def test_transferir_valor_maior_que_carteira_possui(carteiras):
    valor = 1100
    carteira_1,carteira_destino = carteiras
    with pytest.raises(SaldoInsuficienteError):
        transferir(carteira_1,carteira_destino,valor)
    
    assert carteira_1.saldo == 1000
    assert carteira_destino.saldo == 0