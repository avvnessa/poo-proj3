from espiral import Espiral

class Maquina:

    def __init__(self, qtdEspirais: int, maximoProdutos: int):
        self.espirais = self.iniciarEspiraias(qtdEspirais)
        self.maximoDeProduto = maximoProdutos
        self.valor = float(0)
        self.faturamento = 0

    def iniciarEspiraias(self, qtdEspiral: int):
        lista = []
        for x in range(qtdEspiral):
            lista.append(Espiral())
        return lista

    def getFaturamento(self) -> float:
        return self.faturamento

    def getMaximoProdutos(self) -> int:
        return self.maximoDeProduto

    def getSaldoCliente(self) -> float:
        return self.valor

    def getSizeEspirais(self) -> int:
        return len(self.espirais)

    def getEspiral(self, indice: int) -> Espiral:
        if indice < len(self.espirais) and indice >= 0:
            return self.espirais[indice]
        else:
            return None

    def inserirDinheiro(self, value: float) -> bool:
        if value > 0:
            self.valor += value
            return True
        return False

    def receberTroco(self) -> float:
        temp = self.valor
        self.valor = 0
        return temp

    def alterarEspiral(self, indice: int, Nome: str, quantidade: int, preco: float) -> bool:
        espiral = self.getEspiral(indice)
        if espiral is not None and quantidade <= self.maximoDeProduto:
            espiral.setPreco(preco)
            espiral.setQuantidade(quantidade)
            espiral.setNomeDoProduto(Nome)
            return True
        return False

    def limparEspiral(self, indice: int) -> bool:
        espiral = self.getEspiral(indice)
        if espiral is not None:
            self.espirais.pop(indice)
            self.espirais.insert(indice, Espiral())
            return True
        return False

    def vender(self, indice: int) -> bool:
        espiral = self.getEspiral(indice)
        if espiral is not None:
            if espiral.getQuantidade() > 0:
                if self.valor >= espiral.getPreco():
                    espiral.setQuantidade(espiral.getQuantidade() - 1)
                    self.valor -= espiral.getPreco()
                    self.faturamento += espiral.getPreco()
                    if espiral.getQuantidade() == 0:
                        self.limparEspiral(indice)
                    return True
            return False
        return False