import datetime

dia = input().split()
horario = input().split(' : ')
dia2 = input().split()
horario2 = input().split(' : ')

dt1 = datetime.datetime(2022, 4, int (dia[1]), int (horario[0]), int (horario[1]), int (horario[2])) 
dt2 = datetime.datetime(2022, 4, int (dia2[1]), int (horario2[0]), int (horario2[1]), int (horario2[2]))  
tdelta = dt2 - dt1 
tsecs = tdelta.total_seconds()
dias = tsecs // 86400
horas = (tsecs % 86400) // 3600
minutos = ((tsecs % 86400) % 3600) // 60
segundos = ((tsecs % 86400) % 3600) % 60

print('''{:.0f} dia(s)
{:.0f} hora(s)
{:.0f} minuto(s)
{:.0f} segundo(s)'''.format(dias, horas, minutos, segundos))


