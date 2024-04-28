# El problema de "Reciprocal Cycles" se refiere a las fracciones
# unitarias y la longitud de sus ciclos decimales repetitivos.
# Una fracción unitaria es una fracción de la forma 1/n, donde n es un número entero.
# Algunas fracciones unitarias tienen ciclos decimales que se repiten. 
# Por ejemplo, 1/3 = 0.3333... tiene un ciclo de longitud 1.
# El objetivo del problema es encontrar el número menor a 1000 que tiene el ciclo 
# decimal repetitivo más largo.
import time
begin=time.time()
limit=1000

for i in range(1,limit):
    if i%2!=0 and i%5!=0: #Cualquier numero que se puede expresar como 1/2^n*5^m no tiene ciclo pues es 1/10^k
        j=1
        while (10**j-1)%i!=0:
            j+=1
        if j==i-1:
            print(i)
            break

end=time.time()
print("Tiempo de ejecución: ",end-begin)
# Respuesta: 983 - O(n^2)
# merge