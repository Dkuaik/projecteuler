# Problema 31 de Project Euler: Coin Sums
# En Inglaterra, la moneda se compone de:
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) y £2 (200p).
# ¿De cuántas formas se puede hacer £2 usando cualquier cantidad de monedas?

# Solución: La solución que vamos a dar es generando todas las combinaciones posibles de monedas


# Lista de monedas en pence
monedas = [1, 2, 5, 10, 20, 50, 100, 200]
p=200
# Inicializa la lista de maneras
maneras = [0] * (p+1)
maneras[0] = 1

# Para cada tipo de moneda
for moneda in monedas:
    # Para cada cantidad desde moneda hasta 200
    for n in range(moneda, p+1): #el resultado final no se puede tener hasta que se iteren todas las monedas y todos 
        # los valores de n desde la moneda hasta 200 (desde la moneda pues para valores menores es imposible formar combinaciones) 
        maneras[n] += maneras[n - moneda] # se suman las n - moneda, debido a que tomas la moneda en cuenstion y revisas
        #la cantidad de formas para poder formar el resto de la cantidad n.

print(maneras[7])  # Imprime el número de maneras de hacer 200p

#la restpuesta es 73682