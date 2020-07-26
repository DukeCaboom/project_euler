total_sum = 0

def is_palindrome(n):
    return True if n == n[::-1] else False

for i in range(1, 1000000):
    if is_palindrome(str(i)) and is_palindrome(bin(i)[2:]):
        total_sum += i

print(total_sum)