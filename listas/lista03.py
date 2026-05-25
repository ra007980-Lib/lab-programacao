#Dado duas listas de tamanhos diferentes, percorra ambas e intercale seus elementos numa terceira lista. 
#A terceira lista deve começar pelo primeiro elemento da lista menor, e ao fim da lista menor,
#os elementos restantes da lista maior são adicionados no final.
lista1=[1,2,3,4]
lista2=[10,20,30,40,50,60]
lista_intercalada=[]

if len(lista1) < len(lista2):
    menor, maior = lista1, lista2
else:
    menor, maior = lista2, lista1

for i in range(len(menor)):
    if (i < len(menor)):
        lista_intercalada.append(menor[i])
    lista_intercalada.append(maior[i]) #range= Ele gera uma sequência de números para o for contar. Em vez de percorrer os elementos de uma lista, você percorre posições numéricas.
print(f"lista1: {lista1}")
print(f"lista2: {lista2}")
print(f"Lista_intercalada: {lista_intercalada}")