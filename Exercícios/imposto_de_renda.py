valor = float(input())

if valor >= 0 and valor <= 2000.00:
    print("Isento")
elif valor > 4500:
    imposto = (valor - 4500.00)*0.28
    imposto += (4500.00 - 3000.01)*0.18
    imposto += (3000 - 2000.01)*0.08
    print("R$ {:.2f}".format(imposto))
elif valor >= 3000 and valor <= 4500:
    imposto = (valor - 3000.01)*0.18
    imposto += (3000 - 2000.01)*0.08
    print("R$ {:.2f}".format(imposto))
elif valor >= 2000.01 and valor <= 3000:
    imposto = (valor - 2000.01)*0.08
    print("R$ {:.2f}".format(imposto))