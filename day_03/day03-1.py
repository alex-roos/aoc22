file = open("input.txt", "r")
data = file.read().strip().split("\n")
file.close()

file_writer = open("day03_splits.txt", "w")

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

try_n = []

same_count_list = []

match_dict = dict()
match_dict_by_in = dict()

for _sack in rucksacks:
    _c = '??'
    file_writer.write(_sack[1] + "\n")

    
    line_type_set = set()

    _same_count_set = set()
    for _i in _sack[0]:
        if _i in _sack[1]:
            _c = _i
            if _i in match_dict_by_in.keys():
                match_dict_by_in[_i] += 1
            else:
                match_dict_by_in[_i] = 1            
            _same_count_set.add(_i)
            line_type_set.add(_i)
            #break

    try_n.append(list(line_type_set)[0])

    for _x in _sack[0]:
        for _y in _sack[1]:
            if ord(_x) == ord(_y):
                if _x in match_dict.keys():
                    match_dict[_x] += 1
                else:
                    match_dict[_x] = 1
                #break

    same_count_list.append(len(_same_count_set))

    prev_len = len(type_set)
    type_set.add(_c)
    print(f"Line #{line_no}\t", end="")
    line_no+=1

    print(f"1st Half: {_sack[0]} \t2nd Half: {_sack[1]}")

    _temp_print_list = list(type_set)
    _temp_print_list.sort()

    if len(type_set) == prev_len:
        print(f"{_c} already in set {_temp_print_list}")
    else:
        print(f"{_c} added to set {_temp_print_list}")
    #print(f"Shared char: {_c}")
    print()



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


sum_n = 0
for _j in try_n:   
    char_priority = 0
    if _j.isupper():
        char_priority = ord(_j) - 38
    else:
        char_priority = ord(_j) - 96

    sum_n += char_priority


print(f"Custom count: {sum2}")
print(same_count_list)

print(match_dict_by_in)

print(f"Try N: {sum_n}")

file_writer.close()