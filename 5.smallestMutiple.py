#What is the smallest positive number that is evenly 
#divisible by all of the numbers from 1 to 20

for j in range(2,1000000000):
    sM=0
    for i in range(1,21):
        if j%i==0:
           sM+=1
       # print("el modulo es",j%i,j,i,sM) 
    if sM==20:
        break  

print(j)        