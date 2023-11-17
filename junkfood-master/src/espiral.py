class Espiral:

    def __init__(self):
        self.nome = ' - '
        self.quantidade = int(0)
        self.preco = 0

    def getNomeDoProduto(self):
        return self.nome

    def getQuantidade(self):
        return self.quantidade

    def getPreco(self):
        return self.preco

    def setNomeDoProduto(self, nome: str):
        self.nome = nome
        return True

    def setPreco(self, preco: float):
        self.preco = preco
        return True

    def setQuantidade(self, quantidade: int):
        self.quantidade = quantidade
        return True