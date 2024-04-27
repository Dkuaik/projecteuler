import time
import math
inicio=time.time()

a=3
b=2000000
primos=[2]
suma=2

while a<b:
    primo=True
    for i in primos:
        if i>math.sqrt(a):
            break
        if a%i==0:
            primo=False
            break
    if primo:
        primos.append(a)
        suma+=a
    a+=2 #los numeros pares no hace falta probarlos

final=time.time()
print ("La suma es:",suma)
print ("Calculado en",final-inicio,"segundos.")