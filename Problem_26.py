quotients = []
remainders = []
long_rec_cy = 0

def get_len(q):
    sum = 0
    for each in q:
        sum += len(str(each))
    return sum

for n in range(2, 10):
    rem = (1*(10**len(str(n)))) % n
    quo = (1*(10**len(str(n)))) // n
    quotients.append(quo)
    remainders.append(rem)
    if rem != 0:
        while True:
            next_rem = (rem*(10**len(str(n)))) % n
            quo = (rem*(10**len(str(n)))) // n
            if quo != 0 and next_rem not in remainders:
                quotients.append(quo)
                remainders.append(next_rem)
            else:
                break
            rem = next_rem
    quo_len = get_len(quotients)
    if quo_len > long_rec_cy:
        long_rec_cy = quo_len
    print(f"n:{n} quotients: {quotients}")
    quotients = []

print(quotients)
print(long_rec_cy)
