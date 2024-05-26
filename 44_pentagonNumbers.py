# El problema 44 del Proyecto Euler se llama "Pentagon numbers" y se describe de la siguiente manera:

# Los números pentagonales se generan por la fórmula, Pn=n(3n−1)/2. Los primeros diez números pentagonales son:

# 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

# Se puede ver que P4 + P7 = 22 + 70 = 92 = P8. Sin embargo, su diferencia, 70 − 22 = 48, no es pentagonal.

# Encuentra el par de números pentagonales, Pj y Pk, para los cuales su suma y diferencia son pentagonales y D = |Pk − Pj| es minimizado; ¿cuál es el valor de D?

# Solución:

#Importacion de modulo personalizado 

from Modulos import isPentagonal,nth_pentigonalNumber
import itertools

# Inicializacion de variables
i=0
pentagonal_diff=0
pentagonal_sum=0
pentagonal_n=0
pentagonal_m=0
diff=0
# El objetivo es encontrar la diferencia minima entre los numeros pentagonales
# para ello se va a iterar sobre los numeros penagonales, este lo tomamos como la diferencia y calculamos los numeros restantes.
# De esta manera paramos cuando encontremos el primer conjuntos de numeros que cumplan la regla.
# sin perdida de generalidad supongamos que n>m

while not(diff):
    i+=1
    pentagonal_sum=nth_pentigonalNumber(i)
    for n in range(1,i):
        pentagonal_n=nth_pentigonalNumber(n)
        pentagonal_m=pentagonal_sum-pentagonal_n
        pentagonal_diff=abs(pentagonal_n-pentagonal_m)
        if isPentagonal(pentagonal_m) and isPentagonal(pentagonal_diff):
            diff=pentagonal_diff
            break
print(diff)      

