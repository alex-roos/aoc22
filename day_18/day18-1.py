def get_neighbors(_l):

    adjacent_sides = []
    
    idx = 0
    for idx in range(3):
        for _displacement in [-1,1]:
            _foo = list(_l).copy()
            _foo[idx] += _displacement
            adjacent_sides.append(tuple(_foo))

    return adjacent_sides


file = open("C:\\Users\\alex\\dev\\aoc22\\day_18\\day_18_input.txt", "r")
data = file.read().strip().split("\n")

puzzle_input = []

for line in data:
    _x = tuple([int(_i) for _i in line.split(',')])

    puzzle_input.append(_x)

all_sides = dict()
added_cubes = []

for cube in puzzle_input:
    # if tuple(cube) in all_sides:
    #     all_sides.remove(tuple(cube))

    # for _s in get_neighbors(cube):
    #     if _s not in added_cubes:
    #         all_sides.add(_s)

    #     print(all_sides)
    
    # added_cubes.append(tuple(cube))

    all_sides[cube] = []

    for _s in get_neighbors(cube):
       # print(_s)
        if _s in all_sides.keys():
            print("Overlap:", _s)
            all_sides[_s].remove(cube)
        else:
            all_sides[cube].append(_s)

total = 0

for _l in all_sides.values():
    total += len(_l)

print(total)

file.close()