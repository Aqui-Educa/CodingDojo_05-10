from Carro import Carro
from Pessoa import Pessoa
from Vendedor import Vendedor

lista_carro = []
lista_pessoa = []
lista_vendedor = []

carro = Carro("cor", "marca", "modelo", False, 9000, 0, 0)
lista_carro.append(carro)

pessoa = Pessoa("cpf", "nome", "telefone", "email")
lista_pessoa.append(pessoa)

vendedor = Vendedor("cpf", "nome", "telefone", "email", "empresa", "codigo_vendedor")
lista_vendedor.append(vendedor)

km = carro.get_km()
mes = carro.get_mes()
carro.andar(km, mes)

km = carro.get_km()
mes = carro.get_mes()
carro.andar(km, mes)

while(km <= 10000):
    carro.andar(km, mes)
    print(f'Você andou {km} Km\n')
    km += 1000

print('Parabéns, você chegou!!!')