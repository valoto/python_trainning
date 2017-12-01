class Quadrado:
    __lado = 0

    def get_lado(self):
        return self.__lado

    def set_lado(self, lado):
        self.__lado = lado

    def __init__(self, lado):
        self.__lado = lado

    def mudar_lado(self, lado):
        self.set_lado(lado)

    def retorna_lado(self):
        return self.get_lado()

    def calcula_area(self):
        return self.get_lado() * self.get_lado()

#    def calcula_area(self):
#        return self.__lado * self.__lado

quadradinho = Quadrado(2)
print(quadradinho.retorna_lado())
print(quadradinho.calcula_area())
