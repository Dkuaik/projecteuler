# Problema 30 de Project Euler: Potencias de dígitos de quinto orden
#
# Sorprendentemente, hay solo tres números que pueden ser escritos como 
# la suma de las cuartas potencias de sus dígitos:
# 1634 = 1^4 + 6^4 + 3^4 + 4^4
# 8208 = 8^4 + 2^4 + 0^4 + 8^4
# 9474 = 9^4 + 4^4 + 7^4 + 4^4
# Como 1 = 1^4 no es una suma, no se incluye.
# La suma de estos números es 1634 + 8208 + 9474 = 19316.
# Encuentra la suma de todos los números que pueden ser escritos como la 
# suma de las quintas potencias de sus dígitos.


#inicializacion de variables
suma=0
num=1

#mientras el numero sea menor que 1000000

while num<1000000:
    #se obtiene la suma de las potencias de los digitos
    if num==sum([int(x)**5 for x in str(num)]): #se crea el iterador
        #se suma a la suma total
        suma+=num
    #se aumenta el numero
    num+=1
print(suma)