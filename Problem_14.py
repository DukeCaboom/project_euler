
longest_chain = 0
current_chain = 0

for starting_number in range(4, 1000000):
    number = starting_number
    if starting_number % 2 != 0:
        while number != 1:
            if number % 2 == 0:
                number = number / 2 
            else:
                number = ( 3 * number ) + 1
            current_chain += 1
        
        current_chain += 1

        if current_chain > longest_chain:
            longest_chain = current_chain
            print(f"starting_number: {starting_number}, chain_length: {current_chain}")
    current_chain = 0

print(longest_chain)