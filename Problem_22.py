with open("p022_names.txt") as reader:
    names = reader.read().replace("\"", "").split(",")

names.sort()

total_name_score = 0

for pos in range(len(names)):
    name_score = sum([ord(i)-64 for i in names[pos]]) * (pos+1)
    total_name_score += name_score

print(total_name_score)
