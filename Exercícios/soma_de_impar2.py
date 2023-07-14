n = int(input())
inicio = 0
fim = 0
soma = 0
lista = []

for i in range(n):
    num = input().split()
    num[0] = int(num[0])
    num[1] = int(num[1])
    if num[0] > num[1]:
        inicio = num[1]
        fim = num[0]
    elif num[1] > num[0]:
        inicio = num[0]
        fim = num[1]
    else:
        inicio = num[1]
        fim = num[1]
    for j in range(inicio+1, fim):
        if j % 2 == 1:
            soma+=j
    lista.append(soma)
    soma = 0
for somas in lista:
    print(somas)
    
