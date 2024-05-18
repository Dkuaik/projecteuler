from math import sqrt

with open('sources/0042_words.txt','r') as file:
    words = file.read().split(',')

# print(words[:5])
ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ABC_mapping = {ABC[i]:i+1 for i in range(26)} #diccionario que contiene la codificacion
# print(ABDC_mapping['A'])
codified = []
for word in words: #codificando las palabras
    codified.append(sum([ABC_mapping[letra] for letra in word[1:-1]]))
# print(codified[:5])
# Un numero triangula T es triangular si y solo si 8*T+1 es un cuadrado perfecto impar
# Es decir 1/2(-1+sqrt(1+8T)) debe ser un numero natural.

triangularCodifiedNum=[]
for code in codified:
    determinant=1/2*(-1+sqrt(1+8*code))
    if determinant%1==0:
        triangularCodifiedNum.append(code)
print(len(triangularCodifiedNum))
