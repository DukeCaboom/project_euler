greatest_product = 0

def ispalindrome(product):
    return True if str(product) == str(product)[::-1] else False

for i in reversed(range(100, 1000)):
    for j in reversed(range(100, 1000)):
        product = i*j
        if ispalindrome(product):
            print(f"{i} * {j} = {product}")
            if greatest_product < product:
                greatest_product = product
            break

print(greatest_product)