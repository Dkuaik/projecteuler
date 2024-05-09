# Problema 28 de Project Euler: Espiral de números en diagonal
#
# Comenzando con el número 1 y moviéndose hacia la derecha en una 
# espiral de números en forma de cuadrado, se forma una espiral de 5 por 5 de la siguiente manera:
#
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
#
# Se puede verificar que la suma de los números en las diagonales es 101.
#
# ¿Cuál es la suma de los números en las diagonales en una espiral formada de 
# la misma manera que contiene un cuadrado de lado 1001?

# Solución: La solucion que vamos a dar es generando la matriz espiral y posteriormente 
# sumando los elementos de las diagonales
# Hay una segunda solución que consiste en observar que los elementos de las diagonales 
# siguen una secuencia aritmética, por lo que se puede calcular la suma de los elementos 
# (2*k+1)^2
# (2*k+1)^2-2k
# (2*k+1)^2-4k
# (2*k+1)^2-6k
# donde k es el número de espiras que se han recorrido, osea k=1,2,3,...,n-1/2
import time
begin=time.time()
#dimension de la matriz
n=1001
#Creacion de matriz vacia
A=[]
for i in range (n):
    A.append([])
    for j in range (n):
      A[i].append([])

#Creacion de matriz con espiral de numeros
#Inicializacion de variables
a=int((n+1)/2)-1
k=3
count=1
A[a][a]=count
#Para llenar la matriz de la forma espiral se mecesitan 4 ciclos
count+=1
for k in range(1,int((n+1)/2)): #Ciclo para recorrer las espirales
    #Primer ciclo
    for j in range(2*k):
        A[a-(k-1)+j][a+k]=count
        count+=1
    #Segundo ciclo
    for j in range(2*k):
        A[a+k][a+k-j-1]=count
        count+=1
    #Tercer ciclo
    for j in range(2*k):
        A[a+k-j-1][a-k]=count
        count+=1
    #Cuarto ciclo
    for j in range(2*k):
        A[a-k][a-k+1+j]=count
        count+=1

#imprimir matriz
# for i in range (n):
#     print(A[i])

#Suma de los elementos de las diagonales
suma=0
for i in range(n):
    suma+=A[i][i]
    suma+=A[i][n-i-1]

#Se resta el elemento que se repite
suma-=A[int((n-1)/2)][int((n-1)/2)] #el elemento es 1 pero lo podemos generalizar

print("La suma de los elementos de las diagonales es:",suma)
# El resultado es 669171001

end=time.time()
print("Tiempo de ejecución:",end-begin,"segundos")