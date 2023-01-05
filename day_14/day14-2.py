file = open("day_14_input.txt", "r")
data = file.read().strip().split("\n")
file.close()

MAP_WIDTH = 1000
MAP_HEIGHT = 300

grains_of_sand = 25

paths = []

for line in data:
    _curr_x = None
    _curr_y = None

    path_line = []

    _curr_phase = "start"
    _phase_counter = 0

    for _c in line:
        if _curr_phase == "start":
            _curr_x = _c
            _curr_phase = "get_x"
        elif _curr_phase == "get_x":
            if _c == ',':
                _curr_x = int(_curr_x)
                _curr_phase = "get_y"
                _curr_y = ''
            else:
                _curr_x += _c
        elif _curr_phase == "get_y":
            if _c == ' ':
                _curr_y = int(_curr_y)
                path_line.append((_curr_x, _curr_y))
                _curr_phase = "next_point"
            else:
                _curr_y += _c
        elif _curr_phase == "next_point":
            if _phase_counter == 2:
                _curr_phase = "start"
                _phase_counter = 0
            else:
                _phase_counter += 1

    paths.append(path_line + [(_curr_x, int(_curr_y))])

x_pts = []
y_pts = []

for _line in paths:
    for _pt in _line:
        x_pts.append(_pt[0])
        y_pts.append(_pt[1])

print(f"X max: {max(x_pts)}, X min: {min(x_pts)}")
print(f"Y max: {max(y_pts)}, Y min: {min(y_pts)}")

wall_map = [[0]*MAP_WIDTH for _ in range(max(y_pts) + 2)]
# check for falling into abyss if the grain of sand falls below the minimum Y??
wall_map.append([1]*MAP_WIDTH)

for _line in paths:
    _prev_point = None

    for _pt in _line:
        if _prev_point == None:
            _prev_point = _pt
        else:
            #print(f"Working {_prev_point} to {_pt}")
            if _pt[0] == _prev_point[0]:   # check for vertical line
                for _row in range(min([_pt[1], _prev_point[1]]), max([_pt[1], _prev_point[1]])+1):
                    wall_map[_row][_pt[0]] = 1
            elif _pt[1] == _prev_point[1]: # check for horizontal line
                for _col in range(min([_pt[0], _prev_point[0]]), max([_pt[0], _prev_point[0]])+1):
                    wall_map[_pt[1]][_col] = 1

            _prev_point = _pt

falling_into_an_abyss = False
grains_of_sand = 0

max_height = max(y_pts) + 2

while(max_height != 0):
    sand_grain = [500, 0]
    at_rest = False

    grains_of_sand += 1

    #print(f"Max Height of sand is {max_height}")

    while not at_rest:
        if wall_map[sand_grain[1] + 1][sand_grain[0]] == 0:
            sand_grain[1] += 1
        else:
            if wall_map[sand_grain[1] + 1][sand_grain[0] - 1] == 0:
                sand_grain[1] += 1
                sand_grain[0] -= 1
            elif wall_map[sand_grain[1] + 1][sand_grain[0] + 1] == 0:
                sand_grain[1] += 1
                sand_grain[0] += 1
            else:
                wall_map[sand_grain[1]][sand_grain[0]] = 2
                at_rest = True
                if sand_grain[1] < max_height:
                    max_height = sand_grain[1]

    if grains_of_sand % 100 == 0:
        print('='*50 + "Grain #" + str(grains_of_sand) + '='*50)
        # for _row in  range(12):
        #     print(wall_map[_row][490:510])

for _row in range(172):
    print(wall_map[_row][480:520])

print(f"Num grains of sand: {grains_of_sand}")