import math

#Funcion de identificacion de primo
def is_prime ( number:int ) -> bool: 

    """
    Determina si un número es primo.

    Args:
        number (int): El número a evaluar.

    Returns:
        bool: True si el número es primo, False en caso contrario.
    """

    # Evalua los casos base y particulares
    if not isinstance(number,int):   raise ValueError("Only integers are allowed")
    if number<0:                     raise ValueError("Negative values are not allowed")
    if number==0 in [0,1]:           return False
    if number==2:                    return True
    if number%2==0:                  return False
    # Evalua los casos generales
    
    #Teorema matematico el +1 es por el truncado de int() y que el limite superior es abierto
    lim=int(math.sqrt(number)+1) 
    
    for i in range (3,lim,2): #incremento de 2 para no comprobar pares
        if number%i==0:
            return False
    return True  

# Funcion para averiguar el siguiente primo dada una lsita de primos
def nextPrime (p) -> int:
    n=p[-1]+2
    while True:
        if is_prime(n): #esto se depreca por la generacion con yield
            return n
        n+=2

#funcion que genera el n-esimo primo 
def primesGenerator (n: int) -> int: #mejorar algoritmo
    i,j=1,1
    while i<=n:
        j+=1        # utilizar sentencia yield para trabajar con secuencias infinitas
        if is_prime(j):
            i+=1
    return j
