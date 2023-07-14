valores = input().split()

X = float(valores[0])
Y = float(valores[1])

if X > 0 and Y > 0:
    print("Q1")
elif X < 0 and Y > 0:
    print("Q2")
elif X < 0 and Y < 0:
    print("Q3")
elif X > 0 and Y < 0:
    print("Q4")
elif X == 0 and Y != 0:
    print("Eixo Y")
elif X != 0 and Y == 0:
    print("Eixo X")
else:
    print("Origem")