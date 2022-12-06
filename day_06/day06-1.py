file = open("day_06_input.txt", "r")
data = file.read().strip()

file.close()

count_chars = 0

for _i in range(len(data)):
    _temp_set = set()

    _slice = data[_i:_i+4]

    #print(_slice)

    for _j in _slice:
        _temp_set.add(_j)

    if len(_temp_set) == 4:
        print(f"Found unique: {_slice} at {count_chars+4}")
        break

    count_chars += 1