# Problema 38 del Project Euler: Multiplos Pandigitales
#
# Tomemos el número 192 y multipliquémoslo por cada uno de los números 1, 2, y 3:
# 192 × 1 = 192
# 192 × 2 = 384
# 192 × 3 = 576
# Al concatenar todos los productos obtenemos el número 192384576. Podemos ver que este número es un número pandigital de 1 a 9 (es decir, usa todos los dígitos de 1 a 9 exactamente una vez).
#
# El objetivo del problema es encontrar el número entero de 1 a 9 dígitos que tiene esta propiedad de multiplicidad pandigital y que produce el mayor número pandigital de 1 a 9 al concatenar los productos.

import Modulos as md
maxPandigital=0
for n in range(2,9): # el 9 tambien es un valor arbitrario que necesita refactorizacion
    N=[i for i in range (1,n+1)]
    for j in range (1,10000): # 10000 es un valor arbitrario, se necesita refactorizar
        product=""
        for i in N:
            product+=str(i*j)
        if len(product)>9:
            break
        elif len(product)==9:
            if md.isPandigital(product,1,9):
                if int(product)>maxPandigital:
                    maxPandigital=int(product)
print(maxPandigital)
                    
# respuesta: 932718654


# respuesta: 