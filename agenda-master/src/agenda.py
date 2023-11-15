from src.contato import Contato
from src.identificador import Identificador

class Agenda:
    def _init_(self):
        self.contatos = []

    def getContatos(self) -> list:
        return sorted(self.contatos, key=lambda contato: contato.getName())

    def getQuantidadeDeContatos(self) -> int:
        return len(self.contatos)

    def getContato(self, nome: str) -> Contato:
        for contato in self.contatos:
            if contato.getName() == nome:
                return contato
        return None

    def adicionarContato(self, contato: Contato) -> bool:
        if contato.getQuantidadeFones() > 0:
            if contato.getName() in [c.getName() for c in self.contatos]:
                # Contato já existe, adiciona os novos fones ao contato existente
                for c in self.contatos:
                    if c.getName() == contato.getName():
                        c.getFones().extend(contato.getFones())
                        return False
            else:
                # Adiciona um novo contato
                self.contatos.append(contato)
                return True
        return False

    def removerContato(self, nome: str) -> bool:
        for contato in self.contatos:
            if contato.getName() == nome:
                self.contatos.remove(contato)
                return True
        return False

    def removerFone(self, nome: str, index: int) -> bool:
        for contato in self.contatos:
            if contato.getName() == nome:
                return contato.removerFone(index)
        return False

    def getQuantidadeDeFones(self, identificador: Identificador = None) -> int:
        num = 0
        if identificador:
            for contato in self.contatos:
                num += contato.getQuantidadeDeFonesPorId(identificador)
        else:
            for contato in self.contatos:
                num += contato.getQuantidadeFones()
        return num

    def pesquisar(self, expressao: str) -> list:
        resultado = []
        for contato in self.contatos:
            if (
                expressao in contato.getName()
                or any(expressao in fone.getNumero() for fone in contato.getFones())
                or any(expressao in fone.getIdentificador().value for fone in contato.getFones())
            ):
                resultado.append(contato)
        return sorted(resultado, key=lambda contato: contato.getName())