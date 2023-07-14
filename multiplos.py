values = input().split()

A = int(values[0])
B = int(values[1])

if B % A == 0 or A % B == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")