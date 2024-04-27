#Find the difference between the sum of 
#the squares of the first one hundred natural 
#numbers and the square of the sum.Find the difference 
#between the sum of the squares of the first one hundred 
#natural numbers and the square of the sum.
sum1=0
sum2=0
for i in range (1,101):
    sum1+=i**2
    sum2+=i

print(sum1)
print(sum2**2)
