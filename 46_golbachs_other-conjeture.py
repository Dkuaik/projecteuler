# Problema 46 de Project Euler: Conjetura de Goldbach
#
# Christian Goldbach propuso la conjetura de que "todo número impar compuesto puede ser escrito como la suma de un número primo y el doble de un cuadrado".
# Por ejemplo, 9 = 7 + 2*1^2, 15 = 7 + 2*2^2, 21 = 3 + 2*3^2, etc.
# Sin embargo, esta conjetura se demostró incorrecta.
#
# El problema 46 del Project Euler nos pide encontrar el número impar compuesto más pequeño que no puede ser escrito como la suma de un número primo y el doble de un cuadrado.

import Modulos as md
i=0
ans=0
for num in range (1,10000,2): #se itera sobre los numeros impares
    if not(md.is_prime(num)):
        for i in range(1,num):
            if num-2*i**2<=0: #Esta sentencia solo se ejecuta si no encontro uan convinacion de nuemro que cumpla la conjetura, es importante ejecutar esta sentacnia antes que la anterios para evitar valores negativos en la resta num-2*i**2
                ans=num
                break
            if md.is_prime(num-2*i**2): #esta sentacia para romper el ciclo si se cumple la conjetura
                break
    if ans:
        break
print(ans) #respuesta 5777