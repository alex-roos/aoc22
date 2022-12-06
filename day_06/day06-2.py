file = open("day_06_input.txt", "r")
data = file.read().strip()

file.close()

count_chars = 0

for _i in range(len(data)):
    _temp_set = set()

    _slice = data[_i:_i+14]

    #print(_slice)

    for _j in _slice:
        _temp_set.add(_j)

    if len(_temp_set) == 14:
        print(f"Found unique: {_slice} at {count_chars+14}")
        break

    count_chars += 1

# 2253 not correct - missed the offset in the solution print