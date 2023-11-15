from typing import Type


from src.cliente.tipo import Tipo

class Funcionario:

    def __init__(self, cpf: str, nome: str, cargo: Tipo):
        self.cpf = cpf
        self.nome = nome
        self.salario = float(0)
        self.salarioMes = 1
        self.cargo = cargo

    def getNome(self) -> str:
        return self.nome

    def getCpf(self) -> str:
        return self.cpf

    def getSalario(self) -> float:
        return self.salario

    def getCargo(self):
        return self.cargo

    def getQtdDiaria(self):
        return self.diaria

    def getClasse(self):
        return self.classe

    def getNivel(self):
        return self.nivel

    def getInsalubre(self):
        return self.insalubre