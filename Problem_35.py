import gmpy2

def get_cir_combinations(n):
    cir_com = [n]
    for i in range(0, len(n)-1):
        cir_com.append(n[1:] + n[0])
        n = n[1:] + n[0]
    return cir_com


def is_cir_prime(cir_comb):
    for each in cir_comb:
        if not gmpy2.is_prime(int(each)):
            return False
    return True


n = 2
counter = 1


cir_primes = []


while n < 1000000:
    cir_comb = get_cir_combinations(str(n))
    if is_cir_prime(cir_comb):
        cir_primes.append(n)
    # print(f"n: {n} cir_comb: {cir_comb}")
    n = gmpy2.next_prime(n)




print(len(cir_primes))