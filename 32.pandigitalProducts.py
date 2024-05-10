# Euler 32: encontrar productos pandigitales
# Un producto es pandigital si:
# Multiplicando dos números, el producto, multiplicador y multiplicando
# forman un pandigital 1-9. Sin repetir dígitos ni usar el 0.
# Objetivo: suma de todos los productos pandigitales únicos


# Solución:
digits="123456789"
pandigitales = set()
# pandigitales.add(frozenset([1,2,3]))
limite=10000
pentigonales=[]

for i in range (limite):
    for j in range (limite):
        producto = i * j
        if producto > limite:
            break
        if "".join(sorted(str(i) + str(j) + str(producto))) == digits:
            pandigitales.add(producto)
            pentigonales.append([i,j,producto])

print(pandigitales) # se utiliza un set para que no se repitan los productos
print(len(pentigonales))
print(sum(pandigitales)) # 45228