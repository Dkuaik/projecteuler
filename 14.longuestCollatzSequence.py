import Modulos as md 

maxLong=1
n=1
for i in range (1,1000000):
    long=len(md.collatzSequence(i))
    if maxLong<long:
        maxLong=long
print ("La longuitud máxima es",maxLong)  

# print(f"la secuancia es {md.collatzSequence(n)}, con longuitud {len(md.collatzSequence(n))}")