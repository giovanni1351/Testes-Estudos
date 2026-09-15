from projeto.exceptions.saldo_insuficiente import SaldoInsuficienteError


class CarteiraDigital:
    def __init__(self, saldo_inicial=0, log_path=" carteira .log "):
        self.saldo = saldo_inicial
        self.log_path = log_path

    def depositar(self, valor: float):
        self.saldo += valor
        with open(self.log_path, "a") as f:
            f.write(f" deposito :{valor}\n")

    def sacar(self, valor: float):
        if valor > self.saldo:
            raise SaldoInsuficienteError
        self.saldo -= valor
        with open(self.log_path, "a") as f:
            f.write(f" deposito :{valor}\n")
