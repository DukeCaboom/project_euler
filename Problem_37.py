import gmpy2

n = 7
truncatable_primes = []

def is_right_truncatable(n):
    if len(str(n)) == 1:
        return True if gmpy2.is_prime(n) else False
    else:
        if is_right_truncatable(int(str(n)[1:])):
            return True if gmpy2.is_prime(n) else False
        else:
            return False

def is_left_truncatable(n):
    if len(str(n)) == 1:
        return True if gmpy2.is_prime(n) else False
    else:
        if is_left_truncatable(int(str(n)[:-1])):
            return True if gmpy2.is_prime(n) else False
        else:
            return False


while True:
    n = gmpy2.next_prime(n)
    if is_right_truncatable(n) and is_left_truncatable(n):
        truncatable_primes.append(n)
    if len(truncatable_primes) == 11:
        break

print(truncatable_primes)
print(sum(truncatable_primes))