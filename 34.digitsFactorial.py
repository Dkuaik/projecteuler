# Euler 34: Suma de factoriales de dígitos
# 145 es un número curioso ya que 1! + 4! + 5! = 1 + 24 + 120 = 145
# Encuentra la suma de todos los números que son iguales a la suma del factorial de sus dígitos
# Nota: como 1! = 1 y 2! = 2 no son sumas no se cuentan como soluciones

import math
# este limite se puede calcular con la interseccion entre las 2 funciones n! y n
# ya que la suma de los factoriales de los digitos de un numero n crece más rápido que n
factorials=[]
# encontrando limite para n (cuando esta condicion se cumple ya no existe numero superior que 
# cumpla la condicion)
limit=1
while math.factorial(9)*len(str(limit))>limit:
    limit+=1
print(limit)

# Aproximacion de m numero de digitos para encontrar el limite
# potencia_10=lambda m: sum([10**i for i in range(m)])
# m=1
# while potencia_10(m)/(math.factorial(9)*m)<1:
#     m+=1
# print(10**m)

for i in range (11,limit):
    suma=0
    for j in str(i):
        suma+=math.factorial(int(j))
    if suma==i:
        factorials.append(i)
    limit+=1

print(sum(factorials))