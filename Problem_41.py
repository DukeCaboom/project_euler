import gmpy2

def digits_repeated(numbers):
    return False if len(numbers) == len(set(numbers)) else True

def is_1_through_n(n):
    n_list = list(range(1, len(str(n))+1))
    
    status = True if set([str(a) for a in n_list]) == set(str(n)) else False
    # print(n, status)
    return status

def is_pandigital(n):
    status = True if (not digits_repeated([n for n in str(n)])) and is_1_through_n(n) and ('0' not in str(n)) else False
    # print(n, status)
    return status

n = 10
large_pandigital_prime = 10

while True:
    n = gmpy2.next_prime(n)
    if len(str(n)) > 9:
        break
    if is_pandigital(n) and large_pandigital_prime < n:
        large_pandigital_prime = n

print(large_pandigital_prime)