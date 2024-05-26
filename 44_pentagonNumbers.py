# El problema 44 del Proyecto Euler se llama "Pentagon numbers" y se describe de la siguiente manera:

# Los números pentagonales se generan por la fórmula, Pn=n(3n−1)/2. Los primeros diez números pentagonales son:

# 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

# Se puede ver que P4 + P7 = 22 + 70 = 92 = P8. Sin embargo, su diferencia, 70 − 22 = 48, no es pentagonal.

# Encuentra el par de números pentagonales, Pj y Pk, para los cuales su suma y diferencia son pentagonales y D = |Pk − Pj| es minimizado; ¿cuál es el valor de D?

# Solución:

#Importacion de modulo personalizado 

from Modulos import isPentagonal,nth_pentigonNumber

# Inicializacion de variables
i=1
diff=10000
# recorrido sobre i,j,k
diff_nmin=lambda i:3*i-2
pentigonals=[1]
while diff>=diff_nmin(i):
    i+=1
    pentigonals.append(nth_pentigonNumber(i))
    for pj in pentigonals[:-1]:
        pi=nth_pentigonNumber(i)
        # pj=nth_pentigon(j)
        if isPentagonal(pi-pj) and isPentagonal(pi+pj):
        # if isPentagonal(pi):
            if pi-pj<diff:
                diff=pj-pj
                print(pi,pj,diff)
                break
    a=diff_nmin(i+1)
print(diff)