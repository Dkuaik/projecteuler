#Funcion que identifica si una tercia de numeros forman una terna pitagorica
def isPhytagorean (a:int , b:int , c:int) -> bool:
       if a**2+b**2==c**2 or b**2+c**2==a**2 or c**2+a**2==b**2: #esto para que el orden no importe
            return True
       else:
             return False
       
def factors (n: int) -> list:
    factors=list()
    if n==1:
        factors.append([1,1])
        return factors
    for i in range (1,n):
        p=primesGenerator(i)
        potencia=0
        while n%p==0:
            n=n/p
            potencia+=1
        if potencia!=0:
            factors.append([p,potencia])
        if n==1:
            return factors 

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
def properDivisors(n:int):
    divisors=[]
    for i in range(1,n):
        if n%i==0:
            divisors.append(i)
    return divisors