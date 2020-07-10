def ntow(n):
    word = ""
    if  n == 1000:
        word ="onethousand"
        return word
    if 100 <= n <=1000:
        q,r = divmod(n, 100)
        hundreds = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
        word += hundreds[q] + "hundred"
        n = r
        if r!=0:
            word += "and"
    if 20 <= n <=100:
        q,r = divmod(n, 10)
        tens = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}
        word += tens[q]
        n = r
    if 0 < n <= 19:
        ones = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven",
                12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}
        word += ones[n]

    return word


letter_count = 0
for i in range(1, 1001):
    letter_count += len(ntow(i))

print(letter_count)
