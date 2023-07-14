values = input().split()

for i in range(3):
    values[i] = float (values[i])
values2 = sorted(values.copy(), reverse=True)


A = float(values2[0])
B = float(values2[1])
C = float(values2[2])

if A > 0 and B > 0 and C > 0:
    if A >= (B+C):
        print("NAO FORMA TRIANGULO")
    elif (A*A) == ((B*B) + (C*C)):
        print("TRIANGULO RETANGULO")
    elif (A*A) > ((B*B) + (C*C)):
        print("TRIANGULO OBTUSANGULO")
    elif (A*A) < ((B*B) + (C*C)):
        print("TRIANGULO ACUTANGULO")
    if A == B and B == C:
        print("TRIANGULO EQUILATERO")
    elif A == B or A == C or B == C:
        print("TRIANGULO ISOSCELES")
