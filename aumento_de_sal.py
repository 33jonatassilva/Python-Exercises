salario = float(input())


if salario >= 0 and salario <= 400.0:
    reajuste = salario*0.15
    print('''Novo salario: {:.2f}
Reajuste ganho: {:.2f}
Em percentual: 15 %'''.format((salario+reajuste), reajuste))
    
elif salario >= 400.01 and salario <= 800.0:
    reajuste = salario*0.12
    print('''Novo salario: {:.2f}
Reajuste ganho: {:.2f}
Em percentual: 12 %'''.format((salario+reajuste), reajuste))

elif salario >= 800.01 and salario <= 1200.0:
    reajuste = salario*0.10
    print('''Novo salario: {:.2f}
Reajuste ganho: {:.2f}
Em percentual: 10 %'''.format((salario+reajuste), reajuste))

elif salario >= 1200.01 and salario <= 2000.0:
    reajuste = salario*0.07
    print('''Novo salario: {:.2f}
Reajuste ganho: {:.2f}
Em percentual: 7 %'''.format((salario+reajuste), reajuste))

elif salario > 2000.0:
    reajuste = salario*0.04
    print('''Novo salario: {:.2f}
Reajuste ganho: {:.2f}
Em percentual: 4 %'''.format((salario+reajuste), reajuste))