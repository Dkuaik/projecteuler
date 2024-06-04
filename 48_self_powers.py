# the series 
# 1**1+2**2+3**3+4**4+5**5+6**6+7**7+8**8+9**9+10**10=10405071317
# Find the last ten digits of the series 
# 1**1+2**2+3**3+4**4+...+1000**1000
import time
begin=time.time()
ans=0
for i in range(1,1000):
    ans+=i**i
end=time.time()
print("timepo de ejecusion",end-begin)
ans=str(ans)
print(ans[-10:])
# ans=9110846700