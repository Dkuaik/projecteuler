# Problema 47 de Project Euler: Números con factores primos distintos
#
# El problema nos pide encontrar el primer número de cuatro números consecutivos que tienen cuatro factores primos distintos cada uno.
# Por ejemplo, consideremos los dos números consecutivos 14 = 2 × 7 y 15 = 3 × 5. Ambos tienen dos factores primos distintos.
# Pero el problema nos pide encontrar cuatro números consecutivos, cada uno de los cuales tiene cuatro factores primos distintos.
from Modulos import factors
ans=0
i=134000
while not(ans):
    print(i)
    factors_num=[]
    i+=1
    nums=[i,i+1,i+2,i+3]
    for num in nums:
        factors_num.append([i for i,j in factors(num)])
    if all([len(f)==4 for f in factors_num]):
        ans=i
        break
print(ans) #respuesta 134043