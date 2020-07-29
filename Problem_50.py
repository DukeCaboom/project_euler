import gmpy2

all_primes = []

def trunc_left(n):
    if len(n) == 1:
        return sum(n), len(n)
    if gmpy2.is_prime(sum(n)):
        return sum(n), len(n)
    else:
        return trunc_left(n[1:])

def trunc_right(n):
    if len(n) == 1:
        return sum(n), len(n)
    if gmpy2.is_prime(sum(n)):
        return sum(n), len(n)
    else:
        return trunc_right(n[0:len(n)-1])

n = 0
total_sum = 0

while True:
    n = gmpy2.next_prime(n)
    all_primes.append(n)
    if sum(all_primes) >= 1000000:
        all_primes.remove(n)
        break

print(all_primes)
print(sum(all_primes))

max_left = trunc_left(all_primes)
max_right = trunc_right(all_primes)

print(max_left)
print(max_right)



