
def sum_of_even_fib(a, b, sum):
    next_fib = a + b
    if next_fib < 4000000:
        if next_fib % 2 == 0:
            sum = sum + next_fib
            return sum_of_even_fib(b, next_fib, sum)
        else:
            return sum_of_even_fib(b, next_fib, sum)
    return sum


if __name__ == "__main__":
    first_fib = 1
    second_fib = 2
    print(sum_of_even_fib(1, 2, 2))



