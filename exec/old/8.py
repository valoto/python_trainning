expressao = input("Insira a expressao: ")
numeros = expressao.split('+')
total = 0

for n in numeros:
    total += int (n)

with open ('8.txt', 'w') as f:

    f.write("Entrada: %s\n" % expressao)
    f.write("Total: %s\n"% total)
    


