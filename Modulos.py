# Este es el modulo de las funciones principales que tenga que utilizar
# Para dar solucion a los problemas de Euler
import math

#Funcion de identificacion de primo
def esPrimo ( n:int ) -> bool: 
    if n==2:
         return True
    if n==1 or n== 0:
        return False
    lim=int(math.sqrt(n)+1)  #Teorema matematico el +1 es por el truncado de int() y que el limite superior es abierto
    if n%2==0:
        return False
    for i in range (1,lim,2): #incremento de 2 para no comprobar pares
        if i==1:
            continue
        if n%i==0:
            return False
    return True      

#funcion que genera el n-esimo primo 
def generadorPrimos (n: int) -> int: #mejorar algoritmo
    i,j=1,1
    
    while i<=n:
        j+=1        
        if esPrimo(j):
            i+=1
    return j

#Funcion que identifica si una tercia de numeros forman una terna pitagorica
def isPhytagorean (a:int , b:int , c:int) -> bool:
       if a**2+b**2==c**2:
            return True
       else:
             return False

def factors (n: int):
    factors=list()
    if n==1:
        factors.append([1,1])
        return factors
    for i in range (1,n):
        p=generadorPrimos(i)
        potencia=0
        while n%p==0:
            n=n/p
            potencia+=1
        if potencia!=0:
            factors.append([p,potencia])
        if n==1:
            return factors 
        
def numFactors (n:int , p):
    np=[]
    for i in p:
        if(i>n):break
        j=0
        npj=0
        while n%i==0:
            n/=i
            npj+=1
        np.append(npj)
        j+=1
    num=1
    if n!=1:
        return False
    for i in np:
        num*=(i+1)
    return num


# funcion generadora de numeros triangulares

def numTriangular (n:int) -> int:
    return int((n*(n+1))/2)

#Crea el siguiente elemento de la sucesión partiendo del numero n

def collatz (n:int):
    if (n%2==0):
        return n/2
    else:
        return 3*n+1

#Genera la sucesion de Collatz

def collatzSequence (n:int):
    CS=[]
    CS.append(n)
    while n!=1:
        n=collatz(n)
        CS.append(n)
    # CS.append(n)
    return CS

# Funcion que calcula el factorial de un numero
def factorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
