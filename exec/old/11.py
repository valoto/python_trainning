menu = """
MENU
1- SOMA
2- DIVISAO
3- DIVISAO
4- MULTIPLICACAO

DIGITE UMA OPCAO: 
"""

def soma (a, b):
    return (int(a)+int(b))

def div (a,b):
    return (int(a)/int(b))

def sub (a,b):
    return (int(a)-int(b))

def mult (a,b):
    return (int(a)*int(b))

operacao = 0

while (operacao < 1 or operacao > 4):
    operacao = int(input(menu))
numero1=int(input("Digite o primeiro numero: "))
numero2=int(input("Digite o segundo numero: "))

if operacao == 1:
    print("Total soma: %f" % soma(numero1,numero2))
elif operacao == 2:
    print("Total subtração: %f" % sub(numero1,numero2))
elif operacao == 3:
    print("Total divisao: %f" % div(numero1,numero2))
elif operacao == 4:
    print("Total multiplicacao: %f" % mult(numero1,numero2))
