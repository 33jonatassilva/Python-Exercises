valores = input().split()

N1 = float(valores[0])
N2 = float(valores[1])
N3 = float(valores[2])
N4 = float(valores[3])

media = ((N1*2) + (N2*3) + (N3*4) + (N4*1))/10

print("Media: {:.1f}".format(media))


if media >= 7.0:
    print("Aluno aprovado.")

elif media < 5.0:
    print("Aluno reprovado.")

else:
    print("Aluno em exame.")
    nex = float(input())
    print("Nota do exame: {:.1f}".format(nex))
    media = (media + nex) / 2.0
    if media >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: {}".format(media))
