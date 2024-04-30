from models.contato import Contato


class Mensagem:
    def __init__(self, destinatario: Contato, mensagem: str, dataCriacao: str) -> None:
        self.destinatario = destinatario
        self.mensagem = mensagem
        self.dataCriacao = dataCriacao