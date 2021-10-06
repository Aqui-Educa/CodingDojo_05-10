from Carro import Carro
from Pessoa import Pessoa
from Vendedor import Vendedor

lista_carro = []
lista_pessoa = []
lista_vendedor = []

# # Carros
# cor = input('Cor do carro: ')
# marca = input('Marca do carro: ')
# modelo = input('Modelo do carro: ')
# status = bool(input('Status do carro: '))
# valor = float(input('Valor do carro: '))

carro = Carro("cor", "marca", "modelo", False, 9000, 0, 0)
lista_carro.append(carro)

# # Pessoa
# cpf = input('CPF do comprador: ')
# nome = input('Nome do comprador: ')
# telefone = input('Telefone do comprador: ')
# email = input('Email do comprador: ')

pessoa = Pessoa("cpf", "nome", "telefone", "email")
lista_pessoa.append(pessoa)

# # Vendedor
# cpf = input('CPF do vendedor: ')
# nome = input('Nome do vendedor: ')
# telefone = input('Telefone do vendedor: ')
# email = input('Email do vendedor: ')
# empresa = input('Empresa do vendedor: ')
# codigo_vendedor = input('Código do vendedor: ')

vendedor = Vendedor("cpf", "nome", "telefone", "email",
                    "empresa", "codigo_vendedor")
lista_vendedor.append(vendedor)

# Venda
# vendedor.venda(carro, pessoa)
# pessoa.venda(carro, pessoa)

km = carro.get_km()
mes = carro.get_mes()
carro.andar(km, mes)

