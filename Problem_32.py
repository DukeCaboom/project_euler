
pandigital_products = []

def digits_repeated(numbers):
    return False if len(numbers) == len(set(numbers)) else True


for i in range(1, 9999):
    if (not digits_repeated([n for n in str(i)])) and '0' not in str(i):
        for j in range(1, 9999):
            if ((not digits_repeated([n for n in str(j)]))) and '0' not in str(j):
                product = i*j
                if ((not digits_repeated([n for n in str(product)])) and '0' not in str(product)):
                    mmp = str(i) + str(j) + str(product)
                    if len(mmp) > 9:
                        break
                    if len(mmp) == 9 and (not digits_repeated([n for n in mmp])) and (product not in pandigital_products):
                        print(f"i:{i} j:{j} p:{product}")
                        pandigital_products.append(product)


print(pandigital_products)
print(sum(pandigital_products))




