valores = input().split()
A = float(valores[0])
B = float(valores[1])
C = float(valores[2])

triangulo = (A*C)/2
circulo = 3.14159*(pow(C,2))
trapezio = ((A+B)*C)/2
quadrado = pow(B,2)
retangulo = A*B

print('''TRIANGULO: {:.3f}
CIRCULO: {:.3f}
TRAPEZIO: {:.3f}
QUADRADO: {:.3f}
RETANGULO: {:.3f}'''.format(triangulo, circulo, trapezio, quadrado, retangulo))