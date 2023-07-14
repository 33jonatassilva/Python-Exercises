n = int(input())
media = 0
lista = list()
for i in range(n):
    valores = input().split()

    
    media = ((float(valores[0])*2) + (float(valores [1])*3) + (float(valores [2])*5))/10
    lista.append(media)

for i in range(n):
    print("{:.1f}".format(lista[i]))
