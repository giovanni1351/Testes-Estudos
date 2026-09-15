from carteira_digital import CarteiraDigital


def transferir(origem: CarteiraDigital, destino: CarteiraDigital, valor: float):
    origem.sacar(valor)
    destino.depositar(valor)
