# from sympy import primerange, isprime, prevprime

# def find_largest_prime(x):
#     half_x = prevprime((x//2) + 1)
#     while(half_x > 1):
#         print(f"half_x: {half_x}\n x % half_x: {x % half_x}")
#         if x % half_x == 0:
#             return half_x
#         half_x = prevprime(half_x)
#     return x

# if __name__ == "__main__":
#     if isprime(600851475143):
#         print("600851475143 is prime")
#     else:
#         print(find_largest_prime(600851475143))


from multiprocessing import Pool

data = [
    [1, 100000]
]

def get_first_half(a_list):
    if abs(a_list[0] - a_list[1]) <=50000:
        return a_list
    else:
        mid = ( a_list[0] + a_list[1] ) // 2
        a_list.append(get_first_half([a_list[0], mid ]))
        a_list.append(get_second_half([mid, a_list[1]]))
        return a_list

def get_second_half(a_list):
    if abs(a_list[0] - a_list[1]) <=50000:
        return a_list
    else:
        mid = ( a_list[0] + a_list[1] ) // 2
        a_list.append(get_first_half([a_list[0], mid ]))
        a_list.append(get_second_half([mid, a_list[1]]))
        return a_list


def mp_do_split(a):
    print(f"a: {a}")
    # mid_v = (a[0] + a[1]) // 2
    # return [a[0], mid_v], [mid_v + 1, a[1]]
    mid_v = a[0] + a[1] // 2
    return [[a[0], mid_v], [mid_v + 1, a[1]]] 

def get_mid(a):
    return (a[0] + a[1] ) // 2

def mp_handler():
    global data
    print(f"data: {data}")
    while data[0][1] >= 5000:
        new_list = []
        p = Pool(2)
        split_list = p.map(mp_do_split, data)
        print(f"split list: {split_list}")
        for each in split_list:
            for a in each:
                print
            new_list.append(a for a in each)
        print(f"new data list: {new_list}")
        data = new_list
    # print(f"final data list: {data}")

if __name__ == '__main__':
    mp_handler()


    # a = 1
    # # b = 600851475143
    # b = 200000
    # final_list = [[a, b]]
    # mid = (a + b) // 2
    # while mid >= 5000:
    #     new_list = []
    #     with Pool(5) as p:
    #         a = p.map(do_split, final_list)
    #     print(a)
    #     new_list.append(a)
    #     new_list.append(b)
    #     # for each in final_list:
    #     #     split_list = do_split(each)
    #         # print(split_list)
    #         # for e in split_list[0]:
    #         #     print(e)
    #         #     new_list.append(e)
    #     print(f"new_list: {new_list}")
    #     final_list = new_list
    #     print(f"final list: {final_list}")
    #     mid = final_list[0][1]
    # print(final_list)

    # # with Pool(5) as p:
    # #     a = list(p.map(get_mid, [[1, 3126], [3127, 6251], [6252, 12502], [12503, 12501]]))
    # #     print(a)

    # # with Pool(5) as p:
    # #     # print(p.map(get_mid, [[1, 200000], []]))