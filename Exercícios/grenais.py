resp = 0
cont = 0
gols = []
golsdef = []
sint = 0
sgre = 0
empa = 0

while resp != 2:
    gols = input().split()
    golsdef.append(gols)
    
    if gols[0] > gols [1]:
        sint += 1
    elif gols[0] < gols[1]:
        sgre += 1
    else:
        empa += 1
    cont+=1
    
    resp = int(input('Novo grenal (1-sim 2-nao)\n'))

if sint > sgre:
    print('''{} grenais
Inter: {}
Gremio: {}
Empates: {}
Inter venceu mais'''.format(cont, sint, sgre, empa))
elif sint < sgre:
    print('''{} grenais
Inter: {}
Gremio: {}
Empates: {}
Gremio venceu mais'''.format(cont, sint, sgre, empa))
else:
    print('''{} grenais
Inter: {}
Gremio: {}
Empates: {}
Nao houve vencedor'''.format(cont, sint, sgre, empa))



