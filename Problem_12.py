from functools import reduce

def factors(n):
    return list(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5)+1) if n%i == 0 ))))

n = 1
pos = 1
while True:
    if len(factors(n)) > 500:
        break
    pos += 1
    n = n + pos

print(pos)
print(n)
