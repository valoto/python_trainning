with open ('arq.txt', 'a') as f:
    f.write('Nova Linha\n')

with open ('arq.txt', 'r') as f:
    for l in f.readlines():
        print("Linha: %s" %l)
