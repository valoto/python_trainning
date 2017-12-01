menu = """
MENU
1- INSERIR
2- SAIR

DIGITE UMA OPCAO: 
"""

def main():
    operacao = 1
    while (operacao > 0 or operacao < 2):
        operacao = int(input(menu))
        if operacao == 5:
            break
        entrada()
        if operacao == 1:
            insere()
        elif operacao == 2:
            break

def entrada():
    global nome, email
    nome = input("NOME: ")
    email = input("EMAIL: ")

def insere():
    with open ('13.txt', 'a') as f:
        f.write("Nome: %s       | Email: %s\n" % (nome, email))

main()
