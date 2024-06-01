from modules.special_number import factorial

def lexicographicPermutation(n:int) -> list:
    n-=1
    digits = [0,1,2,3,4,5,6,7,8,9]
    permutation = []
    for i in range(10):
        index = n // factorial(9-i)
        n = n % factorial(9-i)
        permutation.append(digits.pop(index)) 
    return permutation

# Esta funcion genera la n-esima permutacion de un conjunto de numeros
def permutations(numbers):
    if len(numbers) == 1:
        return [numbers]
    result = []
    for i in range(len(numbers)):
        rest = numbers[:i] + numbers[i+1:]
        for p in permutations(rest):
            result.append([numbers[i]] + p)
    return result

def nth_permutation(numbers, m):
    # Genera todas las permutaciones
    perms = permutations(numbers)
    # Ordena las permutaciones
    perms.sort()
    # Devuelve la m-ésima permutación
    return perms[m-1]
# genera el n-simo numero pentagonal

