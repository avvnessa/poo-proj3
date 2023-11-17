from src.espiral import Espiral


class Maquina:

    def __init__(self, qtdEspirais: int, maximoProdutos: int):
        pass

    def getFaturamento(self) -> float:
        return 0.0

    def getMaximoProdutos(self) -> int:
        return 0

    def getSaldoCliente(self) -> float:
        return 0.0

    def getSizeEspirais(self) -> int:
        return 0

    def getEspiral(self, indice: int) -> Espiral:
        return None

    def inserirDinheiro(self, value: float) -> bool:
        return False

    def receberTroco(self) -> float:
        return 0.0

    def alterarEspiral(self, indice: int, nome: str, quantidade: int, preco: float) -> bool:
        return True

    def limparEspiral(self, indice: int) -> bool:
        return True

    def vender(self, indice: int) -> bool:
        return False
