# Problema 29 de Project Euler: Potencias distintas
#
# Considera todas las potencias enteras a^b para 2 ≤ a ≤ 5 y 2 ≤ b ≤ 5:
# 2^2=4, 2^3=8, 2^4=16, 2^5=32
# 3^2=9, 3^3=27, 3^4=81, 3^5=243
# 4^2=16, 4^3=64, 4^4=256, 4^5=1024
# 5^2=25, 5^3=125, 5^4=625, 5^5=3125
# Si se eliminan las repeticiones, obtenemos 15 términos distintos.
# ¿Cuántos términos distintos se generan al considerar todas las potencias 
#  enteras a^b para 2 ≤ a ≤ 100 y 2 ≤ b ≤ 100?


# Solución: La solución que vamos a dar es generando todas las potencias enteras a^b

potencias=set()

for a,b in [(a,b) for a in range(2,101) for b in range(2,101)]:
    potencias.add(a**b)

print(len(potencias))

# el resultado es 9183