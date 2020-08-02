x = 1
block = 1
result = 1
while True:
    if len(str(6 * x)) > len(str(x)):
        block += 1
        x = 10 ** block
    elif '5' in str(x) or '0' in str(x):
        print(f"x: {x}")
        x2 = 2 * x
        x3 = 3 * x
        x4 = 4 * x
        x5 = 5 * x
        x6 = 6 * x
        if sorted(str(x)) == sorted(str(x2)) and sorted(str(x3)) == sorted(str(x4)) and sorted(str(x)) == sorted(str(x4)) and sorted(str(x5)) == sorted(str(x6)) and sorted(str(x)) == sorted(str(x5)):
            print(f"x2:{x2} x3:{x3} x4:{x4} x5:{x5} x6:{x6}")
            result = x
            break
        else:
            x += 1
    else:
        x += 1

print(result)
