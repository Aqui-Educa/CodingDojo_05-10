class Carro:
    def __init__(self, cor, marca, modelo, status, valor, km, mes):
        self._cor = cor
        self._marca = marca
        self._modelo = modelo
        self._status = status
        self._valor = valor
        self._km = km
        self._mes = mes

    # Getters e Setters
    def get_cor(self):
        return self._cor

    def set_cor(self, cor):
        self._cor = cor

    def get_marca(self):
        return self._marca

    def set_marca(self, marca):
        self._marca = marca

    def get_modelo(self):
        return self._modelo

    def set_modelo(self, modelo):
        self._modelo = modelo

    def get_status(self):
        return self._status

    def set_status(self, status):
        self._status = status

    def get_valor(self):
        return self._valor

    def set_valor(self, valor):
        self._valor = valor

    def get_km(self):
        return self._km

    def set_km(self, km):
        self._km = km

    def get_mes(self):
        return self._mes

    def set_mes(self, mes):
        self._mes = mes

    def ligar(self):
        if(self._status == True):
            self._status = False
            print('Carro foi desligado!')
        else:
            self._status = True
            print('Carro foi ligado!')

    def revisao(self, km, mes):
        if km == 1000 or mes == 3:
            print("Efetue a primeira revisão do seu veiculo!\n"
                  " A proxima revisão será aos 4000km ou 6 meses")
        elif km == 4000 or mes == 9:
            print("Efetue a segunda revisão do seu veiculo!\n"
                  "A proxima revisão será aos 10000km ou 6 meses")
        else:
            print("Seu carro não precisa de revisão")

    def andar(self, km, mes):
        km = km + 1000
        self.set_km(km)
        mes = mes + 1
        self.set_mes(mes)
        self.revisao(km, mes)
        return km

    def multa(self, limite):
        while True:
            velocidade = float(input(f'Seu carro estava a quantos km/h? '))
            try:
                assert velocidade > 0
            except:
                print('Velocidade não pode ser menor ou igual a 0')
                continue

            print(f'Você passou a {velocidade} e o limite é {limite}')
            
            if velocidade > limite:
                print('Você foi multado!')
            break