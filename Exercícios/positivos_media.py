cont = 0
media = 0
for i in range (6):
    num = float(input())
    if num > 0:
        cont+=1
        media += num
print("{} valores positivos".format(cont))
print('{:.1f}'.format(media/cont))