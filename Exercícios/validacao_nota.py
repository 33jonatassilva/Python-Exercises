soma = 0
cont = 0
resp = 0

while True:
    try:
        n = float(input())
    except EOFError:
        break
        
    if n >= 0 and n <= 10:
        soma += n
        cont += 1
        if cont == 2:
            print('media = {:.2f}'.format(soma/2))
            while resp != 1 and resp != 2:
                resp = int(input('novo calculo (1-sim 2-nao)\n'))
            if resp == 1:
                soma = 0 
                cont = 0
                resp = 0
                continue
            else:
                break
    else:
        print('nota invalida')