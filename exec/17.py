class Pessoa:
    __nome = ''
    __idade = 0
    __peso = 0
    __altura = 0

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_idade(self):
        return self.__idade

    def set_idade(self, idade):
        self.__idade = idade

    def get_peso(self):
        return self.__peso

    def set_peso(self, peso):
        self.__peso = peso

    def get_altura(self):
        return self.__altura

    def set_altura(self, altura):
        self.__altura = altura

    def __init__(self, nome, idade, peso, altura):
        self.__nome = nome
        self.__idade = idade               
        self.__peso = peso
        self.__altura = altura

    def envelhecer(self, idade):
        self.__idade += idade

    def engordar(self, peso):
        self.__peso += peso

    def emagrecer(self, peso):
        self.__peso -= peso

    def crescer(self, altura):
        self.__altura += altura

joao = Pessoa('Joao', 40, 80, 1.80)
print(joao.get_nome(), joao.get_idade(), joao.get_peso(), joao.get_altura())

joao.envelhecer(10)
joao.engordar(10)
joao.emagrecer(20)
joao.crescer(0.10)

print(joao.get_nome(), joao.get_idade(), joao.get_peso(), joao.get_altura())


#17 - Classe Pessoa: Crie uma classe que modele uma pessoa:
#Atributos: nome, idade, peso e altura
#Métodos: Envelhercer, engordar, emagrecer, crescer.

