var = "PYT''\"HON"
var = 'PYTH"ON'

# TODAS MAIUSCULAS
print(var.upper())

# TODAS MINUSCULAS
print(var.upper())

# SUBSTITUI T POR X
print(var.replace('T', 'X'))

# PRIMEIRA LETRA MAIUSCULA0
print(var.title())

# CONTA QUANTIDADE DE LETRAS T
print(var.count('T'))

# PROCURAR POSIÇÃO DA LETRA T
print(var.find('T'))

# QUANTIDADE DE CARACTERES DA STRING
print(len(var))

# JUNTA UMA LISTA EM UMA STRING
print(', '.join(['a', 'b', 'c']))

# EXPLODE UMA STRING EM UMA LISTA
print(var.split(','))

nome = "Igor"
sobrenome = "Valoto"
idade = 24

print(nome + " " + sobrenome)
print("Meu nome é: %s e tenho %s anos" % (nome, idade))
print("Meu nome é: {0} e tenho {1} anos".format(nome, idade))

var10 = "Meu nome é: {0} e tenho {1} anos".format(nome[:2], idade)

print(var10)


