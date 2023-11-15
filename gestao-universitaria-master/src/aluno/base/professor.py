from src.aluno.base.funcionario import Funcionario
from src.cliente.tipo import Tipo

class Professor(Funcionario):

    def __init__(self, cpf: str, nome: str, classe: str):
        super().__init__(cpf, nome, Tipo.PROF)
        self.classe = classe
        self.diaria = 3