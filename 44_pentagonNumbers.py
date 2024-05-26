# El problema 44 del Proyecto Euler se llama "Pentagon numbers" y se describe de la siguiente manera:

# Los números pentagonales se generan por la fórmula, Pn=n(3n−1)/2. Los primeros diez números pentagonales son:

# 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

# Se puede ver que P4 + P7 = 22 + 70 = 92 = P8. Sin embargo, su diferencia, 70 − 22 = 48, no es pentagonal.

# Encuentra el par de números pentagonales, Pj y Pk, para los cuales su suma y diferencia son pentagonales y D = |Pk − Pj| es minimizado; ¿cuál es el valor de D?

# Solución:

#Importacion de modulo personalizado 

from Modulos import is_pentagonal,nth_pentagonal_number
import itertools

# Inicializacion de variables
i=0
pentagonal_diff=0
pentagonal_sum=0
pentagonal_n=0
pentagonal_m=0
diff=0
# El objetivo es encontrar la diferencia minima entre los numeros pentagonales
# para ello se va a iterar sobre los numeros penagonales, el primero lo declaramos como la suma ya qeu esto marca una cota superior para los demás pantigonales. 
# luego se genera el numero pantigonal n, con n<sum_n así con las relaciones aritmeticas se generan los otros numeros
# la prueba final es revisal que el conjunto de 4 numeros cumple que todos son pantigonales. 
# la primera que pase la prueba es la respuesta, cualquier otro conjunto de numeros tendria una diferencia mayor.
# De esta manera paramos cuando encontremos el primer conjuntos de numeros que cumplan la regla.

while not(diff):
    i+=1
    pentagonal_sum=nth_pentagonal_number(i)
    for n in range(1,i):
        pentagonal_n=nth_pentagonal_number(n)
        pentagonal_m=pentagonal_sum-pentagonal_n
        pentagonal_diff=abs(pentagonal_n-pentagonal_m)
        if is_pentagonal(pentagonal_m) and is_pentagonal(pentagonal_diff):
            diff=pentagonal_diff
            break
print(diff) #respuesta 5482660

