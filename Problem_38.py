largest_pandigital = 0

def digits_repeated(numbers):
    return False if len(numbers) == len(set(numbers)) else True

def is_1_through_n(n):
    n_list = list(range(1, len(str(n))+1))    
    return True if set([str(a) for a in n_list]) == set(str(n)) else False

def is_9_digit_number(n):
    return True if len(str(n)) == 9 else False

def is_gt_9_digit_number(n):
    return True if len(n) > 9 else False

for i in range(1, 10000):
    concat_number = ''
    for j in range(1, 10):
        concat_number += str(i * j)
        if is_gt_9_digit_number(concat_number) or is_9_digit_number(concat_number):
            break
    if is_9_digit_number(concat_number) and is_1_through_n(int(concat_number)) and not digits_repeated([n for n in concat_number]):
        if largest_pandigital < int(concat_number):
            largest_pandigital = int(concat_number)

print(largest_pandigital)


