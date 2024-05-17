# Problema 39 del Project Euler: Triángulos rectángulos enteros
#
# Si p es el perímetro de un triángulo rectángulo con lados de longitud entera,
# {a,b,c}, hay exactamente tres soluciones para p = 120:
# {20,48,52}, {24,45,51}, {30,40,50}
#
# Para qué valor de p ≤ 1000, es el número de soluciones máximo?
# Notese que a,b,c forman una terna pitagorica si y solo si a^2+b^2=c^2 es decir
# a=m^2-n^2, b=2mn,  c=m^2+n^2  con m>n

import Modulos as md
import math
count=0
triada=[]
results=[]

for p in range (840,1001):
    triada=[]
    count=0
    for a in range (1,p//2+1):
        for b in range (1,a+1):
            c_2=a**2+b**2
            c=math.sqrt(c_2)
            if a+b+c==p:
                if math.sqrt(c_2)%1==0:
                    count+=1
                    triada.append([a,b,c])
    if count!=0:results.append([count,p,triada])
results.sort(key=lambda x: x[0])
print(results[-1])
# respuesta: 
 