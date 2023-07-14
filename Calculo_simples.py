entrada = input().split()

codigo = int(entrada[0])
qte = int(entrada[1])
valor = float(entrada[2])

entrada2 = input().split()

codigo2 = int(entrada2[0])
qte2 = int(entrada2[1])
valor2 = float(entrada2[2])

total = qte*valor + qte2*valor2

print("VALOR A PAGAR: R$ {:.2f}".format(total))