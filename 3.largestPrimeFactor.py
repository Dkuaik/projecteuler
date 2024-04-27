#Whats the largest prime factor of the number 600851475143
n=600851475143

#Funcion de identificaci'on de primo
def esPrimo ( n:int ) -> bool:
     
    for i in range (2,n):
        if n%i==0:
            return False
    return True

#funcion que genera el n-esimo primo
def generadorPrimos (n: int) -> int:
    i,j=1,0

    while i<=n:
        j+=1        
        if esPrimo(j):
            i+=1
    return j

for i in range (2,n):
    p=generadorPrimos(i)
    while n%p==0:
        print(f"n es {n} el {i} primo es {generadorPrimos(i)}")
        n=n/p
    #print(n)
    if n==1:
        print(f"el primo mas grande es {p}, y n es {n}")
        break


