import math

lower_bound = 10
upper_bound = 7 * math.factorial(9)

total_sum = 0
for i in range(lower_bound, upper_bound+1):
    fact_digits_sum = sum([math.factorial(int(digit)) for digit in str(i)])
    if fact_digits_sum == i:
        total_sum += fact_digits_sum

print(total_sum)