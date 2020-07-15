from functools import reduce

given_n = 10000

def factors(n):    
    return list(set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5)+1) if n % i == 0))))

amicable_pairs = []

for i in range(2, given_n):
    if i not in amicable_pairs:
        a = sum(factors(i))-i
        b = sum(factors(a))-a
        if i == b and a != b:
            if i not in amicable_pairs:
                amicable_pairs.append(a)
            if b not in amicable_pairs:
                amicable_pairs.append(b)
print(amicable_pairs)
print(sum(amicable_pairs))
