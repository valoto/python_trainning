class Bola:
    __cor = None
    __circ = 0
    __material = None

    def get_cor(self):
        return self.__cor

    def set_cor(self, cor):
        self.__cor = cor

    def get_circ(self):
        return self.__circ

    def set_circ(self, circ):
        self.__circ = circ

    def get_material(self):
        return self.__material

    def set_material(self, material):
        self.__material = material

    def __init__(self, cor, circ, material):
        self.__cor = cor
        self.__circ = circ
        self.__material = material

    def trocar_cor(self, cor):
        self.set_cor(cor)
        
    def mostrar_cor(self):
        return self.get_cor()

#INSTANCIANDO E DEFININDO OBJETO
objeto = Bola('Azul', 3.15, 'Plastico')
#PRINTANDO  OBJETO
print(objeto.get_cor(), objeto.get_circ(), objeto.get_material())

#UTILIZANDO AS FUNÇOES
print(objeto.mostrar_cor())
objeto.trocar_cor('Vermelho')

#PRINTANDO APOS MODIFICACAO
print(objeto.get_cor(), objeto.get_circ(), objeto.get_material())


