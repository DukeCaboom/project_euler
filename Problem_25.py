F1 = 1
F2 = 1
pos = 3

while True:
    next_fib = F1 + F2
    if len(str(next_fib)) >= 1000:
        break
    F1 = F2
    F2 = next_fib
    pos += 1

print(pos)