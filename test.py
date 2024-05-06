import Modulos as md
# n=2*4*13*19*23*43*43*19*19*19*7
# print(md.numFactors(n,[2,3,5,7,11,13,17,19,23,31,37,41,43,47]))
n=13
x=1/n
x_n=x*10**7
print(x_n, "modulo 7: ",int(x_n%n))