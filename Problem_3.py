from functools import reduce
import gmpy2

def factors(n):
    return list(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5)+1) if n%i == 0))))

n_factors = factors(600851475143)

largest = 0

for each in n_factors:
    if gmpy2.is_prime(each) and each > largest:
        largest = each

print(n_factors)
print(largest)