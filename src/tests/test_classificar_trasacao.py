import pytest
from projeto.classificar_trasacao import classificar_transacao


@pytest.mark.parametrize("valor, classe",[
    (50,"pequena",),
    (99,"pequena",),
    (100,"media",),
    (200,"media",),
    (999,"media",),
    (1000,"grande",),
    (2000,"grande",),
    (1001,"grande",),
])
def testar_classificacoes_de_transacao(valor,classe):
    assert classificar_transacao(valor) == classe