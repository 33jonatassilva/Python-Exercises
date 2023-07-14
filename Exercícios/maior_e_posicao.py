lista = list()
maior = 0


for i in range(100):
    num = int(input())
    if num > maior:
        maior = num
        pos = i
print(maior)
print(pos+1)