import Modulos as md
import time as tm

p=[]
i=0
np=1
j=1
nt=0
while np<500:
    i+=1
    nt+=i
    np=1
    if (md.isPrime(nt)):
        continue
    while (not (md.numFactors(nt,p))):
        # if (md.esPrimo(j)): p.append(j)
        p.append(md.primesGenerator(j))
        j+=1
    np=md.numFactors(nt,p)
    long=len(p)
# print(p)
print(f"El numero {nt} tiene {np} divisores el número de fueron necesarios es {long}")