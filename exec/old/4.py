numeros = []

while len(numeros) < 5:
    numeros.append(int(input("")))    

total = 0

for n in numeros:
    total += n

print ("Media é: %i" % (int(total)/len(numeros)))
