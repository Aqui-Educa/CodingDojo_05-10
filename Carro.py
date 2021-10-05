class Carro:
    def __init__(self, cor, marca, modelo, status):
        self._cor = cor
        self._marca = marca
        self._modelo = modelo
        self._status = status
    
    def get_cor(self):
        return self._cor
    def set_cor(self, cor):
        pass
    
    def ligar(self):
        if(self._status == True):
            self._status = False
            print('Carro foi desligado!')
        else:
            self._status = True
            print('Carro foi ligado!')