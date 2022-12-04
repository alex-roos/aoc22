file = open("day_03_input.txt", "r")
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
    rucksacks.append([line[:int(len(line)/2)], line[int(len(line)/2):]])
_c = '??'
sum = 0
type_set = set()

line_no = 1

same_count_list = []

match_dict = dict()

for _sack in rucksacks:
    
    _same_count_set = set()
    for _i in _sack[0]:
        if _i in _sack[1]:
            _c = _i
            #break
            _same_count_set.add(_i)
            
    for _x in _sack[0]:
        for _y in _sack[1]:
            if _x == _y:
                match_dict[_x] = 1

    same_count_list.append(len(_same_count_set))

    prev_len = len(type_set)
    type_set.add(_c)
    print(f"Line #{line_no}\t", end="")
    line_no+=1

    print(f"1st Half: {_sack[0]} \t2nd Half: {_sack[1]}")

    if len(type_set) == prev_len:
        print(f"{_c} already in set.")
    else:
        print(f"{_c} added to set")
    #print(f"Shared char: {_c}")



print(type_set)
print(match_dict.keys())

try1 = list(type_set)
try2 = list(match_dict.keys())

try1.sort()
try2.sort()

print(try1)
print(try2)


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
print(same_count_list)
file.close()