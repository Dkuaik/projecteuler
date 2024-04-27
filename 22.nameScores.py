# El problema de los Name Scores implica la manipulación de una lista de nombres.
# Primero, se nos proporciona un archivo de texto de 46K que contiene más de cinco mil 
# nombres de primer orden alfabéticamente.
# Para cada nombre, debemos sumar los valores alfabéticos de sus letras (donde A=1, B=2, ..., Z=26) 
# y luego multiplicar la suma por la posición del nombre en la lista.
# Por último, debemos sumar estos valores para todos los nombres en el archivo para obtener el 
#"score" total.


with open('sources/names.txt', 'r') as file:
    names = file.read().split(',')
names = [name.replace('"', '') for name in names]
names=sorted(names)

# Crear un diccionario de letras y sus valores alfabéticos
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letter_values = {letters[i]: i + 1 for i in range(len(letters))}

# Calcular el score total
i=0
scores=[]
for name in names:
    i+=1
    score = sum([letter_values[letter] for letter in name])*i
    scores.append(score)
print (sum(scores))