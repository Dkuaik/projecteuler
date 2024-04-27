#Funcion de identificacion de primo
def esPrimo ( n:int ) -> bool:
     
    for i in range (2,n):
        if n%i==0:
            return False
    return True

#funcion que genera el n-esimo primo
def generadorPrimos (n: int) -> int:
    i,j=0,0

    while i<=n:
        j+=1        
        if esPrimo(j):
            i+=1
    return j

n=generadorPrimos(10001)
print(f"El 10001st primo es {n}")
