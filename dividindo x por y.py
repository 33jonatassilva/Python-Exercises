n = int(input())

for i in range(n):
    valors = input().split()
    valors[0] = int(valors[0])
    valors[1] = int(valors[1])
    if valors[1] == 0:
        print('divisao impossivel')
    else:
        print('{:.1f}'.format(valors[0]/valors[1]))

