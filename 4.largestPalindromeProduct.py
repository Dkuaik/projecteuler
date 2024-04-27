def isPalindrome (n:str) -> bool:
    
    for i in range (1,int(len(n)/2)+1):
        if n[i-1]!=n[-i]:
            #print(f"las entradas {n[i-1]} y {n[-i]} son distintas")
            return False
    return True
#n=str(948849)
#r=isPalindrome(n)
#print (f"el numero {n} palindromo {r}")
palindormes=list()
for i in range (1,1000):
    for j in range (1,1000):
        i1=1000-i
        j1=1000-j
        if isPalindrome(str(i1*j1)):
            r=i1*j1
            #print(f"El palindormo producto mas grande es {i1} x {j1} = {r}")
            palindormes.append([i1*j1,i1,j1])
            break
palindormes.sort()
print(f"El palindromo mas grande es {palindormes[-1]}")