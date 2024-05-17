# se tiene que onostruir un programa que determine el numero primo pantigonal más grande
# que exista.

# Su pongamso que el numero más grande que se puede formar en un pantigonal 9 (1-9), 
# es decir que el pantigonal 10 está excluido por definición ambigua

import Modulos as md

for n in range (1,10):
    lim_sup=10**(n-1)
    lim_inf= 1 if n-1<1 else 10**(n-2)
    for i in range (lim_inf,lim_sup):
        pentigonal=md.isPandigital(str(i),1,n-1)
        if pentigonal:
            primo=md.esPrimo(i)
            if primo:
                maxPP=i
print(maxPP)
# esto esta hecho a la fuerza bruta, pero hay una forma mucho m'as efectiva
# Se puede tomar el conjunto (1,2,..,n) y sacar todas sus permutaciones
# Preguntar si alguno de esos numeros es primo, de esta forma los calculos se reducen mucho
