num = int(input())
cont = 0
aux = num
while cont < 6:
    if aux % 2 == 1:
        print(aux)
        cont+=1
    aux+=1

