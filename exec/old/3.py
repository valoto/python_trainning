i = 0

numeros = []

while i < 5:
    numeros.append(input())
    if i == 0:    
        maior = numeros[0]
    else:
        if numeros[i] > maior:
            maior = numeros[i]    
    i += 1

print("O maior numero é: " + maior)
 
    

