file = open("day_03_input_test.txt", "r")
data = file.read().strip().split("\n")

rucksacks = []
priority_values = dict()

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWYXZ"

_i = 1
for _l in letters:
    priority_values[_l] = _i
    _i+= 1

print(priority_values)

for line in data:
    rucksacks.append([line[:int(len(line)/2 - 1)], line[int(len(line)/2):]])

_c = '1'
sum = 0
type_set = set()

for _sack in rucksacks:
    for _i in _sack[0]:
        if _i in _sack[1]:
            _c = _i
            break
    prev_len = len(type_set)
    type_set.add(_c)
    if len(type_set) == prev_len:
        print(f"{_c} already in set.")
    else:
        print(f"{_c} added to set")
    #print(f"Shared char: {_c}")

print(type_set)

for _c in type_set:   
    char_priority = 0
    if _c.isupper():
        char_priority = ord(_c) - 38
    else:
        char_priority = ord(_c) - 96

    sum += char_priority

#948 was too low, 7540 was too high
print(f"Answer: {sum}")

sum2 = 0

for _t in type_set:
    sum2 += priority_values[_t]

print(f"Custom count: {sum2}")

file.close()