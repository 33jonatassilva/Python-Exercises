
n1 = str(input())
n2 = str(input())
n3 = str(input())

dicionário = {'vertebrado':{'ave':{'carnivoro':'aguia', 'onivoro':'pomba'}, 'mamifero':{'onivoro':'homem', 'herbivoro':'vaca'} },'invertebrado':{'inseto':{'hematofago':'pulga', 'herbivoro':'lagarta'}, 'anelideo':{'hematofago':'sanguessuga', 'onivoro':'minhoca'}}}

nome = (dicionário[f'{n1}'][f'{n2}'][f'{n3}'])
print(nome)

