class Pessoa:
    def __init__(self, cpf, nome, telefone, email):
        self._cpf = cpf
        self._nome = nome
        self._telefone = telefone
        self._email = email

    # Getters e Setters
    def get_cpf(self):
        return self._cpf

    def set_cpf(self, cpf):
        self._cpf = cpf

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    def get_telefone(self):
        return self._telefone

    def set_telefone(self, telefone):
        self._telefone = telefone

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    def venda(self, carro, pessoa):
        print(f'Exemplo.....')    