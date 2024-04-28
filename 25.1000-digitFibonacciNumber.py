# El problema consiste en encontrar el primer número de Fibonacci que tiene 1000 
# dígitos. Los números de Fibonacci se generan sumando los dos números anteriores 
# de la secuencia, comenzando con 1 y 2. El objetivo es encontrar el primer número 
# de Fibonacci que tiene exactamente 1000 dígitos y escribir un programa para calcularlo.

import Modulos as md
i=0
while len(str(md.fibonacci(i)))<1000:
    i+=1
print(f"El primer numero de Fibonacci con 1000 digitos es: {i}. {md.fibonacci(i)}")

# respuesta: 4782