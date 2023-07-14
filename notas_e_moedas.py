from decimal import Decimal

N = Decimal(input())

cem = int(N / Decimal('100'))
N = N % Decimal('100')

cinqu = int(N / Decimal('50'))
N = N % Decimal('50')

vinte = int(N / Decimal('20'))
N = N % Decimal('20')

dez = int(N / Decimal('10'))
N = N % Decimal('10')

cinco = int(N / Decimal('5'))
N = N % Decimal('5')

dois = int(N / Decimal('2'))
N = N % Decimal('2')

um = int(N / Decimal('1'))
N = N % Decimal('1')

mcin = int(N / Decimal('0.50'))
N = N % Decimal('0.50')

mvin = int(N / Decimal('0.25'))
N = N % Decimal('0.25')

mdez = int(N / Decimal('0.10'))
N = N % Decimal('0.10')

mcinco = int(N / Decimal('0.05'))
N = N % Decimal('0.05')

mum = int(round(N / Decimal('0.01')))

print(f'''NOTAS:
{cem} nota(s) de R$ 100.00
{cinqu} nota(s) de R$ 50.00
{vinte} nota(s) de R$ 20.00
{dez} nota(s) de R$ 10.00
{cinco} nota(s) de R$ 5.00
{dois} nota(s) de R$ 2.00
MOEDAS:
{um} moeda(s) de R$ 1.00
{mcin} moeda(s) de R$ 0.50
{mvin} moeda(s) de R$ 0.25
{mdez} moeda(s) de R$ 0.10
{mcinco} moeda(s) de R$ 0.05
{mum} moeda(s) de R$ 0.01''')
