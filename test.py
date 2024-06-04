# import modules.primes as primes

def nums():
    i=0
    while True:
        i+=1
        yield i
numeros=nums()        
print(next(numeros))