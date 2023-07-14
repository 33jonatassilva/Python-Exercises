pares = 0 
impares = 0
positivos = 0
negativos = 0
for i in range (5):
    num = float(input())
    if num % 2 == 0:
        pares+=1
    elif num % 2 == 1:
        impares+=1
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1 
print('''{} valor(es) par(es)
{} valor(es) impar(es)
{} valor(es) positivo(s)
{} valor(es) negativo(s)'''.format(pares, impares, positivos, negativos))