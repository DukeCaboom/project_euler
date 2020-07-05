import gmpy2

limit = 2000000

def primes():
    n = 2
    while n <= limit:
        yield n
        n = gmpy2.next_prime(n)

prime_numbers_below_10 = primes()
print(sum(list(prime_numbers_below_10)))