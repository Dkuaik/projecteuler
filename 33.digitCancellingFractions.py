# Euler 33: Fracciones curiosas
# Hay 4 fracciones de menos de 1, con 2 dígitos en numerador y denominador
# Que pueden simplificarse de manera no convencional cancelando un dígito común
# Ejemplo: 49/98 = 4/8 al cancelar el 9
# Encuentra el denominador de la fracción resultante al multiplicar estas 4 fracciones

fracciones=[]
for i in range (11,100):
    for j in range (i+1,100):
        if i%10 == 0 or j%10 == 0:
            continue
        frac=i/j
        i_str=str(i)
        j_str=str(j)
        if i_str[0] in j_str:
            j_str=j_str.replace(i_str[0],'',1)
            i_str=i_str.replace(i_str[0],'',1)
            frac2=int(i_str)/int(j_str)
            if frac==frac2:
                fracciones.append([int(i_str),int(j_str)])
        elif i_str[1] in j_str:
            j_str=j_str.replace(i_str[1],'',1)
            i_str=i_str.replace(i_str[1],'',1)
            frac2=int(i_str)/int(j_str)
            if frac==frac2:
                fracciones.append([int(i_str),int(j_str)])
numerador=1
denominador=1
print(fracciones) 
for i in fracciones: #multiplicando todas las fracciones
    numerador*=i[0]
    denominador*=i[1]
print(numerador,denominador) #8/800 -> 1/100  