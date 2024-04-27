# El problema de las "Non-Abundant Sums" se refiere a los números que no pueden ser 
# escritos como la suma de dos números abundantes. Un número abundante es un número 
# que es menor que la suma de sus divisores propios (excluyendo el mismo número).
# Por ejemplo, 12 es el número abundante más pequeño porque 1 + 2 + 3 + 4 + 6 = 16 > 12.
# El objetivo es encontrar la suma de todos los números positivos que no pueden ser 
# escritos como la suma de dos números abundantes.
import Modulos as md
import time
begin=time.time()
# abd_nums = []
# for i in range(1, 28124):
#     if sum(md.properDivisors(i))>i:
#         abd_nums.append(i)
# # print(abd_nums)
# not_abd_nums = []
# for k in range(1,28124):
#     for i in abd_nums:
#         for j in abd_nums:
#             if i+j==k or i+j>k:
#                 break
#         else:
#             not_abd_nums.append(k)
#             continue
#         break
#     else:
#         pass
# print(not_abd_nums)
# print(sum(not_abd_nums))    
limit = 28124
abundant_nums = [i for i in range(1, limit) if sum(md.properDivisors(i)) > i]
sums_of_two_abundants = [False] * limit

for i in range(len(abundant_nums)):
    for j in range(i, len(abundant_nums)):
        if abundant_nums[i] + abundant_nums[j] < limit:
            sums_of_two_abundants[abundant_nums[i] + abundant_nums[j]] = True
        else:
            break

not_abundant_sums = [i for i, x in enumerate(sums_of_two_abundants) if not x]
end=time.time()
print(sum(not_abundant_sums))
print("Tiempo de ejecución:",end-begin)