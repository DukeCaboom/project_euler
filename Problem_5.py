from functools import reduce
import gmpy2

def factors(n):
    return list(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5)+1) if n%i == 0 ))))

my_numbers = [i for i in range(1, 21)]

n = 2520
while True:
    f_n = factors(n)
    if all(item in f_n for item in my_numbers):
        break
    n += 1
    if n%10000 == 0:
        print(n)

print(n)

