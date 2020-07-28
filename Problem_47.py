from functools import reduce

lower_bound = 644


def factors(n):
    return list(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5)+1) if n%i == 0  ))))

n0 = 644
n1 = 645
n2 = 646
n3 = 647

while True:
    
    print(factors(644))

