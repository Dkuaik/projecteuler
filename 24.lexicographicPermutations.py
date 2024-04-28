# El problema de las "Lexicographic Permutations" se refiere a la generación de permutaciones 
# en orden lexicográfico. Dada una secuencia de elementos, una permutación lexicográfica 
# implica reorganizar los elementos en el orden "siguiente" lexicográficamente.
# Por ejemplo, dada la secuencia [0, 1, 2], las permutaciones lexicográficas son:
# [0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0].
# El objetivo es encontrar la permutación n-ésima en orden lexicográfico de una secuencia dada.
#What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

import Modulos as md

n=2504860
permutation = md.lexicographicPermutation(n)
print(permutation)

# Respuesta: 2783915460
# esto funciona de la siguiente manera:
    # 1. Se crea una lista de los dígitos del 0 al 9.
    # 2. Se calcula el primer digito, dependiendo de que numero de permutacion se busque.
        # 2.1 Va por niveles para el primer digito el orden es de 9!, pues son las primeras 9! permutaciones
        # 2.2 se recalcula n, que es el resto de la division de n entre 9! pues ya sacamos el primer digito
        # 2.3 Se calcula el siguiente digito, el orden es de 8! pues son las siguientes 8! permutaciones
    # 3. Se elimina el digito de la lista. y se agrega a la permutacion