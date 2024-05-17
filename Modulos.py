# Este es el modulo de las funciones principales que tenga que utilizar
# Para dar solucion a los problemas de Euler
import math

# Funcion para detectar numeros pandigitales
def isPandigital (n:str,a,b) -> bool:
    pantiDigit=str(n)
    for i in range (a,b+1):
        if str(i) in pantiDigit:
            pantiDigit=pantiDigit.replace(str(i),'',1)
        else:
            return False
    if pantiDigit=='':
        return True
    else:
        return False


# Funcion para detectar palindromos

def isPalindrome (n:str) -> bool:
    n=str(n)
    for i in range (1,int(len(n)/2)+1):
        if n[i-1]!=n[-i]:
            #print(f"las entradas {n[i-1]} y {n[-i]} son distintas")
            return False
    return True

#Funcion que genera el n-esimo numero de fibonacci
def fibonacci (n:int) -> int:
    if n==0:
        return 0
    if n==1:
        return 1
    a,b=0,1
    for i in range (n-1):
        a,b=b,a+b #aisnacion de los nuevos numeros de fibonacci
    return b

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

# Funcion para averiguar el siguiente primo dada una lsita de primos
def nextPrime (p) -> int:
    n=p[-1]+2
    while True:
        if esPrimo(n):
            return n
        n+=2

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
       if a**2+b**2==c**2 or b**2+c**2==a**2 or c**2+a**2==b**2: #esto para que el orden no importe
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

# fucni'on que descompone en primos con una lista de primos previamente calculada p
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
    if n <= 0:
        return 1
    else:
        return n * factorial(n-1)
    
# funcion que regresa los divisores propios de un numero
def properDivisors(n:int):
    divisors=[]
    for i in range(1,n):
        if n%i==0:
            divisors.append(i)
    return divisors

# esta funcion 

def lexicographicPermutation(n:int) -> list:
    n-=1
    digits = [0,1,2,3,4,5,6,7,8,9]
    permutation = []
    for i in range(10):
        index = n // factorial(9-i)
        n = n % factorial(9-i)
        permutation.append(digits.pop(index)) 
    return permutation

# Esta funcion genera la n-esima permutacion de un conjunto de numeros
def permutations(numbers):
    if len(numbers) == 1:
        return [numbers]
    result = []
    for i in range(len(numbers)):
        rest = numbers[:i] + numbers[i+1:]
        for p in permutations(rest):
            result.append([numbers[i]] + p)
    return result

def nth_permutation(numbers, m):
    # Genera todas las permutaciones
    perms = permutations(numbers)
    # Ordena las permutaciones
    perms.sort()
    # Devuelve la m-ésima permutación
    return perms[m-1]

