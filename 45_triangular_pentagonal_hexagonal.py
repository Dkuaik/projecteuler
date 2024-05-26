# El problema 45 del Proyecto Euler se llama "Triangular, pentagonal, y hexagonal" y se describe de la siguiente manera:

# Los números triangulares se generan al sumar los números naturales. Así que el 7º número triangular sería 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. Los primeros diez términos serían:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# De manera similar, los números pentagonales se generan al sumar los números naturales, pero con una fórmula diferente. Los primeros diez números pentagonales son:

# 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

# Los números hexagonales se generan de una manera similar, y los primeros diez son:

# 1, 6, 15, 28, 45, 66, 91, 120, 153, 190, ...

# Se puede verificar que el número T285 = P165 = H143 = 40755.

# Encuentra el siguiente número triangular que también es pentagonal y hexagonal.

#Solucion

# Este problema se pude resolver facil,ente teniendo pruebas para saber si un numero es triangulas, pentagonal o hexagonal. 
# Iteramos sobre los numeros hexagonales ya que estos crecen más rapido
import time
import Modulos as md
begin=time.time()
ans=0
i=2
while not(ans):
    hexagonal_number=md.nth_hexagonal_number(i)
    # print(i,hexagonal_number)
    if md.is_pentagonal(hexagonal_number): #todo numero hexagonar tambien es triangular
        if hexagonal_number==40755: #este if unicamente para que encuentre el segundo
            i+=1
            continue
        ans=hexagonal_number
    i+=1
end=time.time()
print(hexagonal_number,end-begin)