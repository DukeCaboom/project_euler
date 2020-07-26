totol_sum = 0

def digit_fifth_powers(n):
    return sum([int(i)**5 for i in str(n)])

for i in range(2, 10000000):
    if i == digit_fifth_powers(i):
        totol_sum += i
print(totol_sum)