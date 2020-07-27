
import gmpy2

pandigitals = []

def digits_repeated(numbers):
    return False if len(numbers) == len(set(numbers)) else True


def is_0_through_9(n):
    return True if set([str(a) for a in range(0, 10)]) == set(str(n)) else False


def is_10_digit_number(n):
    return True if len(str(n)) == 10 else False


def is_substring_divisible(n, p):
    
    if len(n) == 3:
        return False if int(n[0:3])%p != 0 else True
    else:
        if is_substring_divisible(n[1:], gmpy2.next_prime(p)):
            return False if int(n[0:3])%p != 0 else True
        else:
            return False


for i in range(1000000000, 10000000000):
    if is_10_digit_number(i) and is_0_through_9(int(i)) and not digits_repeated([n for n in str(i)]):
        if is_substring_divisible(str(i)[1:], 2):
            pandigitals.append(i)
    
print(pandigitals)
print(sum(pandigitals))