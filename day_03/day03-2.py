file = open("day_03_input.txt", "r")
data = file.read().strip().split("\n")

groups_of_three = []

counter = 0
temp_grouping = []

for line in data:
    temp_grouping.append(line)
    counter += 1

    if counter == 3:
        groups_of_three.append(temp_grouping)
        temp_grouping = []
        counter = 0
file.close()
#print(groups_of_three)

type_list = []

for group in groups_of_three:
    common_letter_set = set()

    for _c in group[0]:
        if _c in group[1] and _c in group[2]:
            common_letter_set.add(_c)
            break
    
    type_list.append(list(common_letter_set)[0])

print(type_list)
sum = 0
for _c in type_list:   
    char_priority = 0
    if _c.isupper():
        char_priority = ord(_c) - 38
    else:
        char_priority = ord(_c) - 96

    sum += char_priority

print(sum)