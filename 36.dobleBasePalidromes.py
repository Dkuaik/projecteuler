# Problema 36 de Project Euler: Palíndromos de base doble
# Encuentra la suma de todos los números, menores de un millón,
# que son palíndromos en base 10 y base 2.
# (Por favor, tenga en cuenta que el palíndromo no puede comenzar con cero en ninguna de las bases).

import Modulos as md
palindromes=[]
for i in range (1,1000000):
    if md.isPalindrome(i) and md.isPalindrome(int(bin(i)[2:])):
        palindromes.append([i,bin(i)[2:]])
print(sum([i for i,j in palindromes]))
