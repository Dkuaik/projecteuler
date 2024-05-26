# El problema 43 del Proyecto Euler se llama "Sub-string divisibility" y se describe de la siguiente manera:

# El número 1406357289, es un número pandigital de 0 a 9 porque está formado por cada uno de los dígitos de 0 a 9 en algún orden, pero también tiene una propiedad interesante de subcadena de divisibilidad.

# Permítenos ilustrar esta propiedad. Tomemos los dígitos d1 a d10 como los dígitos decimales sucesivos de izquierda a derecha del número, es decir, d1 es el dígito más a la izquierda y d10 es el dígito más a la derecha.

# Encontramos que las siguientes declaraciones son verdaderas:

# d2d3d4=406 es divisible por 2
# d3d4d5=063 es divisible por 3
# d4d5d6=635 es divisible por 5
# d5d6d7=357 es divisible por 7
# d6d7d8=572 es divisible por 11
# d7d8d9=728 es divisible por 13
# d8d9d10=289 es divisible por 17
# Encontrar la suma de todos los números pandigitales de 0 a 9 que tienen esta propiedad.

# Solución:
from Modulos import permutations
digits=list("0123456789")
pandigitals = permutations(digits)
sum=0
for permutation in pandigitals:
    if int("".join(permutation[1:4])) % 2 != 0:
        continue
    if int("".join(permutation[2:5])) % 3 != 0:
        continue
    if int("".join(permutation[3:6])) % 5 != 0:
        continue
    if int("".join(permutation[4:7])) % 7 != 0:
        continue
    if int("".join(permutation[5:8])) % 11 != 0:
        continue
    if int("".join(permutation[6:9])) % 13 != 0:
        continue
    if int("".join(permutation[7:10])) % 17 != 0:
        continue
    sum+=int("".join(permutation))
print(sum) # 16695334890