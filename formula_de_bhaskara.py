from math import sqrt

valores = input().split()

A = float(valores[0])
B = float(valores[1])
C = float(valores[2])

raiz = (pow(B,2) - (4*A*C))

if raiz < 0 or A == 0:
    print("Impossivel calcular")
else:
    X = (-1*B + sqrt(pow(B,2) - (4*A*C))) / (2*A)
    X2 = (-1*B - sqrt(pow(B,2) - (4*A*C))) / (2*A)
    print('''R1 = {:.5f}
R2 = {:.5f}'''.format(X, X2))

