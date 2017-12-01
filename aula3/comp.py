frutas = ['pera', 'uva', 'maca', 'banana']

nova_lista = []

#for f in frutas:
#    if len(f) == 4:
#        nova_lista.append(f)

#print (nova_lista)

nova_lista = [f for f in frutas if len(f) == 4]

print (len(nova_lista))

if len(nova_lista) != 2:
    print (nova_lista)
else:
    print ('Lista vazia!')


