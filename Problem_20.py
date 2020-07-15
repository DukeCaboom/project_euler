given_n = 100

def product_of(n):
    return 1 if n==1 else n * product_of(n-1)

total_sum = sum([int(i) for i in str(product_of(given_n))])

print(total_sum)