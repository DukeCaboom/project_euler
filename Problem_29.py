powers = []
for a in range(2, 6):
    for b in range(2, 6):
        power = a**b
        if power not in powers:
            powers.append(power)

print(powers)
print(len(powers))