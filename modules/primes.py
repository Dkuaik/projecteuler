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
    if number in [0,1]:           return False
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

# Esta funcion regresa un generador de numeros primos con cada next regresa el siguiente
def primes_generator () -> iter: 
    primes=[]
    number=2 # Se pone la base del iterador
    while True:
        if all(number%prime!=0 for prime in primes):
            primes.append(number)
            yield number
        number+=1

