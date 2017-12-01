menu = """
MENU
1- INSERIR
2- SAIR
3- BUSCAR

DIGITE UMA OPCAO: 
"""

def main():
    global operacao
    operacao = 1
    while (operacao > 0 or operacao < 3):
        operacao = int(input(menu))
        if operacao == 2:
            break
        elif operacao == 3:
            entrada()
            busca()
        elif operacao == 1:
            entrada()
            insere()

def entrada():
    global nome, email
    if operacao == 3:
        email = input("EMAIL: ")
    else:
        nome = input("NOME: ")
        email = input("EMAIL: ")

def insere():
    with open ('14.txt', 'a') as f:
        f.write("%s;%s\n" % (nome, email))

def busca():
    with open ('14.txt', 'r') as f:
        for e in f.readlines():
            e = e.strip('\n')
            e = e.split(';')
            if email == e[1]:
                print("Nome: %s" % e[0])
                encontrado = True
    if encontrado == False:
        print("\nNAO ENCONTRADO\n")

main()
