from src.aluno.base.funcionario import Funcionario
from src.cliente.tipo import Tipo

class STA(Funcionario):

    def __init__(self, cpf: str, nome: str, nivel: int):
        super().__init__(cpf, nome, Tipo.STA)
        self.nivel = nivel
        self.diaria = 1