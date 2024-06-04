# Problema 47 de Project Euler: Números con factores primos distintos
#
# El problema nos pide encontrar el primer número de cuatro números consecutivos que tienen cuatro factores primos distintos cada uno.
# Por ejemplo, consideremos los dos números consecutivos 14 = 2 × 7 y 15 = 3 × 5. Ambos tienen dos factores primos distintos.
# Pero el problema nos pide encontrar cuatro números consecutivos, cada uno de los cuales tiene cuatro factores primos distintos.
from modules.primes import primes_generator,is_prime
import time
ans=0
number=2
primes=[]
factors=[]
begin=time.time()
while not(ans):
    number_factors=list()
    number_aux=number
    if is_prime(number):
        primes.append(number)
        factors.append([number])
        number+=1
        continue
    for prime in primes:
        pow=0
        prime_aux=prime
        while number%prime==0:
            pow+=1
            prime=prime_aux**(pow+1)
        number_aux//=prime_aux**pow
        if pow: number_factors.append(prime_aux**pow)   
        if number_aux==1: break 
    factors.append(number_factors)
    if len(factors)>=1000000:
        ans=1
    number+=1
end=time.time()
# print(factors)
print("Tiempo de ejecusion",end-begin)
print(ans) #respuesta 134043