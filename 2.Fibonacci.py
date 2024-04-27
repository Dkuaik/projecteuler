#By considering the terms in the Fibonacci 
#sequence whose values do not exceed four million, 
#find the sum of the even-valued terms.

def isEven(n:int) -> bool:
    if n%2==0:
        return True
    else:
        False
fn=0
n,m=1,0
sum=0
while True:
    if fn>=4000000:
        break
    if isEven(fn):
        print("ok",fn)
        sum += fn
    fn=n+m  
    m=n
    n=fn
print(sum)
