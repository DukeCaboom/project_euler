import gmpy2
from itertools import islice

def primes():
    n = 2
    while True:
        yield n
        n = gmpy2.next_prime(n)

prime_numbers = primes()
print(next(islice(prime_numbers, 10000, None)))
