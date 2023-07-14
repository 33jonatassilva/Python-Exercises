values = input().split()

h1 = int(values[0])
m1 = int(values[1])
min1 = (h1 * 60) + m1
h2 = int(values[2])
m2 = int(values[3])
min2 = (h2 * 60) + m2

if h1 >= h2 and m1 >= m2:
    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format((((min2+1440) - min1) // 60), ((min2+1440) - min1) % 60))
else:
    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(((min2 - min1) // 60), (((min2 - min1) % 60))))
