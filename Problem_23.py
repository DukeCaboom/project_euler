from functools import reduce

limit = 28123

def factors(n):
    return list(set(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5)+1) if n%i==0))))

def is_abundant(n):
    return True if (sum(factors(n))-n > n) else False

abundant_numbers = []
for i in range(1, limit):
    if is_abundant(i):
        abundant_numbers.append(i)

numbers_below_the_limit_that_cannot_be_sum = list(range(1, limit))

for i in range(0,len(abundant_numbers)):
    j = i
    while j < len(abundant_numbers):
        sum_of_abund_numbers = abundant_numbers[i] + abundant_numbers[j]
        if sum_of_abund_numbers > limit:
            break
        j += 1
        if sum_of_abund_numbers in numbers_below_the_limit_that_cannot_be_sum:
            numbers_below_the_limit_that_cannot_be_sum.remove(sum_of_abund_numbers)



print(abundant_numbers)
print(numbers_below_the_limit_that_cannot_be_sum)
print(sum(numbers_below_the_limit_that_cannot_be_sum))
