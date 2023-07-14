X = int(input())
Y = int(input())

soma = 0
aux = 0

if X < Y:
    aux = X
    for i in range(X, Y):
        if aux != X and aux % 2 == 1:
            soma += aux
        aux+=1
if Y < X:
    aux = Y
    for i in range(Y, X):
        if aux != Y and aux % 2 == 1:
            soma += aux
        aux+=1

print(soma)