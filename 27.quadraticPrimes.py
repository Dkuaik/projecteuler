# El problema 27 de Project Euler se titula "Quadratic Primes" 
#y plantea lo siguiente:
# Dado un polinomio cuadrático de la forma n^2 + an + b, donde 
#|a| < 1000 y |b| ≤ 1000, se busca encontrar el producto de los coeficientes 
#a y b que generen la mayor cantidad de números primos consecutivos al evaluar 
#el polinomio para valores de n desde 0 en adelante.
# En resumen, se busca encontrar los coeficientes a y b que generen la mayor cantidad 
#de números primos consecutivos al evaluar el polinomio n^2 + an + b.
import Modulos as md
polyNom=lambda n,a,b:n**2+a*n+b
maxPrimes=0
for a in range(-999,1000):
    for b in range(-1000,1001):
        n=0
        while md.isPrime(abs(polyNom(n,a,b))):
            n+=1
        else:
            if n>maxPrimes:
                aMax=a
                bMax=b
                maxPrimes=n
                product=a*b
print(f"la expresión n^2 + {aMax}n + {bMax} genera {maxPrimes} números primos consecutivos")
print("El producto de los coeficientes es: ",product)