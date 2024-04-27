# este problema se reduce a la permutaci'on de n elementos
# en los que un tipo se elemento se repite n/2 veces y otro tipo se repite n/2 veces
# por lo que el número de permutaciones posibles es n!/(n/2)!*(n/2)!
# la expresion general de esta ecuacion es n!/y!*x! donde x y y son las repteciones de los elementos
# donde n es el munero total de movimientos posibles
# y n/2 es el número de movimientos en un sentido y n/2 en el otro sentido

import Modulos as md
k=20
n=2*k
num=md.factorial(n)/(md.factorial(n/2)*md.factorial(n/2))
print(f"El número de caminos posibles en una cuadricula de {k}x{k} es {int(num)}")