# El problema de "Reciprocal Cycles" se refiere a las fracciones
# unitarias y la longitud de sus ciclos decimales repetitivos.
# Una fracción unitaria es una fracción de la forma 1/d, donde n es un número entero.
# Algunas fracciones unitarias tienen ciclos decimales que se repiten. 
# Por ejemplo, 1/3 = 0.3333... tiene un ciclo de longitud 1.
# El objetivo del problema es encontrar el número menor a 1000 que tiene el ciclo 
# decimal repetitivo más largo.
import time
begin=time.time()

limit=1000
sec_digits=[]
numbers=[]
for d in range(2,limit):
    if d%2==0 or d%5==0:
        continue
    sec_digits=[]  
    res=1%d
    while True:
        if res in sec_digits:
            break
        else:
            sec_digits.append(res)
            res=res*10%d
    numbers.append((len(sec_digits),d))      
numbers.sort(reverse=True)
print(numbers[0])
end=time.time()
print("Tiempo de ejecución: ",end-begin)
# Respuesta: periodo de 982 con d-983