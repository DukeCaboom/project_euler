if __name__ == "__main__":
    # sum = 0
    list_5 = []
    list_3 = []
    for i in range(0, 100, 5):
        if i%5 == 0:
            list_5.append(i)
    for j in range(100):
        if j%3 == 0:
            list_3.append(j)
    print(list(set(list_3 + list_5)))
    print(sum(list(set(list_3 + list_5))))
