n=100000
sum=0
n_3=(n//3)
if n%3==0:
    n_3-=1
n_5=(n//5)
if n%5==0:
    n_5-=1
n_15=(n//15)
if n%15==0:
    n_15-=1
sum=int(3*int(n_3*(n_3+1))/2+5*int(n_5*(n_5+1))/2-15*(n_15*(n_15+1))/2)
print(sum)