def get_digit(n):
    prev_u_bound, cur_u_bound, block = 0, 0, 0
    while(cur_u_bound < n):
        prev_u_bound = cur_u_bound
        block += 1
        cur_u_bound += block * 9 * (10 ** (block - 1))

    exact_position = ( n - prev_u_bound - 1 ) % block
    digit = (10 ** ( block -1 )) + ( n - prev_u_bound - 1 ) / block

    return int(str(digit)[exact_position])



c_constant = get_digit(1) * get_digit(10) * get_digit(100) * get_digit(1000) * get_digit(10000) * get_digit(100000) * get_digit(1000000)
print(c_constant)
