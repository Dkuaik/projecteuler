# #El problema consiste en contar el número de letras utilizadas para escribir 
# los números del 1 al 1000 en palabras. Por ejemplo, el número 342 se escribe 
# "three hundred and forty-two" y utiliza 23 letras. El objetivo es calcular la 
# suma total de letras utilizadas para escribir todos los números en palabras del 1 al 1000.

# Para resolver este problema, se puede utilizar la función `num2words` del módulo `inflect`

import inflect
p = inflect.engine()
allWords=""
for n in range (1,1001):
    nWord=p.number_to_words(n)
    newWord=nWord.replace(" ","")
    newWord=newWord.replace("-","")
    # print(newWord)
    allWords=newWord+allWords
print(allWords)
print(len(allWords))