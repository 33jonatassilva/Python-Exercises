valores = input().split()
A = int(valores[0])
B = int(valores[1])
C = int(valores[2])

maior = A
if B > maior:
    maior = B
if C > maior:
    maior = C
print("{} eh o maior".format(maior))