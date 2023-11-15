from src.aluno.base.funcionario import Funcionario
from src.cliente.tipo import Tipo

class Terceirizado(Funcionario):

    def __init__(self, cpf: str, nome: str, insalubre: bool):
        super().__init__(cpf, nome, Tipo.TERC)
        self.insalubre = insalubre
        self.diaria = 0