valor = int(input())
if valor > 0 and valor < 1000000:
    cem = valor // 100
    cinqu = (valor % 100) // 50
    vinte = ((valor % 100) % 50) // 20
    dez = (((valor % 100) %50) % 20) // 10
    cinco = ((((valor % 100) %50) %20) %10) // 5
    dois = (((((valor % 100) % 50) % 20 ) % 10) % 5) // 2
    um = ((((((valor % 100) % 50) % 20 ) % 10) %5)%2)//1

    print('''{}
{} nota(s) de R$ 100,00
{} nota(s) de R$ 50,00
{} nota(s) de R$ 20,00
{} nota(s) de R$ 10,00
{} nota(s) de R$ 5,00
{} nota(s) de R$ 2,00
{} nota(s) de R$ 1,00'''.format(valor, cem, cinqu, vinte, dez, cinco, dois, um))

