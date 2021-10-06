class Carro:
    def __init__(self, cor, marca, modelo, status, valor):
        self._cor = cor
        self._marca = marca
        self._modelo = modelo
        self._status = status
        self._valor = valor
    
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

    

    
    def ligar(self):
        if(self._status == True):
            self._status = False
            print('Carro foi desligado!')
        else:
            self._status = True
            print('Carro foi ligado!')