n = int(input())
cobaias = 0
ratos = 0
coelhos = 0
sapos = 0

for i in range(n):
    lista = input().split()
    cobaias+= int(lista[0])
    if lista[1] == 'R':
        ratos += int(lista[0])
    elif lista[1] == 'C':
        coelhos += int(lista[0])
    elif lista[1] == 'S':
        sapos += int(lista[0])





print('''Total: {} cobaias
Total de coelhos: {}
Total de ratos: {}
Total de sapos: {}
Percentual de coelhos: {:.2f} %
Percentual de ratos: {:.2f} %
Percentual de sapos: {:.2f} %'''.format(cobaias, coelhos, ratos, sapos, (coelhos*100)/cobaias, (ratos*100)/cobaias, (sapos*100)/cobaias))