import math

def isPandigital (n:str,first_digit:int,last_digit:int) -> bool:
    #Validacion de entradas
    if n<0:
        return ValueError("Negative values are not allowed")
    if first_digit>last_digit:
        return ValueError("The first digit must be less than the last digit")
    #Codigo de la funcion
    pantiDigit=str(n)
    for i in range (first_digit,last_digit+1):
        if str(i) in pantiDigit:
            pantiDigit=pantiDigit.replace(str(i),'',1)
        else:
            return False
    if pantiDigit=='':
        return True
    else:
        return False

def is_palindrome (n:str) -> bool:
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

# funcion generadora de numeros triangulares

def nth_triangular_number (n:int) -> int:
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
    
def nth_pentagonal_number(n:int) -> int:
    return n*(3*n-1)/2

# Evalua si un numero es pentagonal
def is_pentagonal(n:int) -> bool:
    if (1 + math.sqrt(1 + 24 * n)) % 6 == 0:
        return True
    return False

def is_hexagonal(n:int) -> bool:
    if (1+math.sqrt(1+8*n))%4==0:
        return True
    return False

def nth_hexagonal_number(n:int) -> int:
    return n*(2*n-1)    

def is_triangular(n:int) -> bool:
    if (math.sqrt(1+8*n)-1)%2==0:
        return True
    return False