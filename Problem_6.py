# sum square difference

list_of_1_to_100 = list(range(1,101))
list_of_squares_of_1_to_100 = [i**2 for i in list_of_1_to_100]
print((sum(list_of_1_to_100)**2) - sum(list_of_squares_of_1_to_100))

