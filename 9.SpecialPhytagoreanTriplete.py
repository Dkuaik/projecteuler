#There exists exactly one Pythagorean triplet for which a+b+c=1000
#Find the product abc

#Funcion que identifica si una tercia de numeros forman una terna pitagorica
def isPhytagorean (a:int , b:int , c:int) -> bool:
       if a**2+b**2==c**2:
            return True
       else:
             return False


for a in range(1,1000):   
    for b in range(1,1000):   
        for c in range(1,1000):   
            if a+b+c==1000:
                if isPhytagorean(a,b,c):
                     r=a*b*c
                     break
            else:
                continue
        if isPhytagorean(a,b,c):
                     break      
    if isPhytagorean(a,b,c):
                     break       

print(a,b,c,r)