from pathlib import Path

import pytest

from projeto.carteira_digital import CarteiraDigital


@pytest.fixture
def carteira():
    return CarteiraDigital(saldo_inicial=1000)

@pytest.fixture
def carteiras():
    return CarteiraDigital(saldo_inicial=1000),CarteiraDigital(saldo_inicial=0)


@pytest.fixture(scope="function")
def carteira_com_log():
    arquivo = Path("test_logs.txt")
    if arquivo.exists:
        arquivo.unlink(missing_ok=True)

    carteira = CarteiraDigital(saldo_inicial=1000, log_path="test_logs.txt")

    yield carteira

    if arquivo.exists:
        arquivo.unlink(missing_ok=True)


