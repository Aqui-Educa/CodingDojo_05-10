from Pessoa import Pessoa

class Vendedor(Pessoa):
    def __init__(self, cpf, nome, telefone, email, empresa, codigo_vendedor):
        
        super().__init__(cpf, nome, telefone, email)

        self._empresa = empresa
        self._codigo_vendedor = codigo_vendedor

    # Getters e Setters
    def get_empresa(self):
        return self._empresa

    def set_empresa(self, empresa):
        self._empresa = empresa
    
    def get_codigo_vendedor(self):
        return self._codigo_vendedor

    def set_codigo_vendedor(self, codigo_vendedor):
        self._codigo_vendedor = codigo_vendedor

    def venda(self, carro, pessoa):
        print(f'O carro {carro.get_modelo()} foi vendido por {self.get_nome()}, para {pessoa.get_nome()}')