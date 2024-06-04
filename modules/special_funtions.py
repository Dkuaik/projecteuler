#Funcion que identifica si una tercia de numeros forman una terna pitagorica
from modules.primes import primes_generator

def isPhytagorean (a:int , b:int , c:int) -> bool:
       if a**2+b**2==c**2 or b**2+c**2==a**2 or c**2+a**2==b**2: #esto para que el orden no importe
            return True
       else:
             return False
       
def factors (number: int) -> list:
    factors=list()
    primes=primes_generator()
    if number==1:
        factors.append([1,1])
        return factors
    for i in range (1,number): #se puede mejorar el algoritmo, sigue siendo muy ineficiente
        prime=next(primes)
        potencia=0
        while number%prime==0:
            number=number/prime
            potencia+=1
        if potencia!=0:
            factors.append([prime,potencia])
        if number==1:
            return factors 
print(factors(54645))

def num_of_factors (n:int , p):
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

# funcion que regresa los divisores propios de un numero
def proper_divisors(n:int):
    divisors=[]
    for i in range(1,n):
        if n%i==0:
            divisors.append(i)
    return divisors