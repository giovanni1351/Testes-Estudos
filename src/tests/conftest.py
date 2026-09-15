import pytest

from projeto.carteira_digital import CarteiraDigital


@pytest.fixture
def carteira():
    return CarteiraDigital(saldo_inicial=1000)
