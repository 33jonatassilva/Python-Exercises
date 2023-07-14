n = int(input())

if n < 10000:
    cont = 0
    cout = 0

    for i in range(n):
        x = int(input())
        if x < 10000000 and x > -10000000: 
            if x >= 10 and x <=20:
                cont += 1
            else:
                cout += 1

print("{} in".format(cont))
print("{} out".format(cout))