# Problema 37 del Proyecto Euler
# Encontrar la suma de los once primos que son truncables por la izquierda y derecha.
import Modulos as md
primos=[2,3,5,7]
trnPrimes=[]
i=10
while len(trnPrimes)<11:
    primos.append(md.nextPrime(primos))
    i=primos[-1]
    trncNums=[int(str(i)[j:]) for j in range(len(str(i)))]+[int(str(i)[:j]) for j in range(1,len(str(i)))]
    # primos.append(i)
    print(i)
    if all([num in primos for num in trncNums]):
        trnPrimes.append(i)
            # primos.append(i)
    i+=1
print(trnPrimes)
print(sum(trnPrimes))