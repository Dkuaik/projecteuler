import Modulos as md 

maxLong=1
n=1
collatzNum=1
for i in range (1,1000000):
    long=len(md.collatzSequence(i))
    if maxLong<long:
        maxLong=long
        collatzNum=i
print ("La longuitud máxima es",maxLong, "para el número", collatzNum)  

# print(f"la secuancia es {md.collatzSequence(n)}, con longuitud {len(md.collatzSequence(n))}")