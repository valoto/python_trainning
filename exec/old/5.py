alunos = [{
        "nome": "Gabriel",
        "notas": [
            5, 6, 7 ,2
        ]
    },
    {
        "nome": "Jao",
        "notas": [
            8, 6, 7 ,10
        ]
    }
]

for a in alunos:
    notas = 0
    for n in a['notas']:
        notas += n

    media = int(notas/len(a['notas']))

    if media > 6:
        print("%s aprovado com média %i" % (a['nome'], media))
    else:
        print("%s reprovado com média %i" % (a['nome'], media))
    

