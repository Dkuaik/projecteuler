# Problema 40 de Project Euler: Constante de Champernowne
# Generar un número decimal fraccionario concatenando números naturales
# Encontrar el producto de los dígitos en las posiciones 1, 10, 100, 1000, 10000, 100000, y 1000000

num="0."
i=1
while len(num)<1000002:
    num+=str(i)
    i+=1
j=1 #posicion de las d
d=[]
for i in range(7):
    d.append(int(num[j+1]))
    j*=10
mult=1
for i in d:
    mult*=i
print(mult)