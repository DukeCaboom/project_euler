import gmpy2

n = 33

while True:
    if not gmpy2.is_prime(n) and n%2 != 0:
        you_can = False
        for i in range(1, int((n//2)**0.5)+1):
            a = n - (2*(i**2))
            if gmpy2.is_prime(a):
                print(f"{n} = {a} + 2*{i}sq")
                you_can = True
                break
        if not you_can:
            break
    n += 1

print(n)