file = open("day_09_input.txt", "r")
data = file.read().strip().split("\n")
file.close()


dirs_list = ["R", "L", "U", "D"]
max_dists = dict(zip(dirs_list, [0]*len(dirs_list)))

locs_visited = set()
locs_visited.add((0,0))

print(max_dists)

curr_x = 0
curr_y = 0

# determine size of area covered
for line in data:
    _direction, _magnitude = line.strip().split(" ")
    _magnitude = int(_magnitude)

    if _direction == "R":
        curr_x += _magnitude   
        if curr_x > max_dists["R"]:
            max_dists["R"] = curr_x 
    elif _direction == "L":
        curr_x -= _magnitude
        if curr_x < max_dists["L"]:
            max_dists["L"] = curr_x
    elif _direction == "U":
        curr_y -= _magnitude
        if curr_y < max_dists["U"]:
            max_dists["U"] = curr_y
    elif _direction == "D":
        curr_y += _magnitude
        if curr_y > max_dists["D"]:
            max_dists["D"] = curr_y

print(max_dists)

tail_loc = [0,0]
head_loc = [0,0]

for line in data:
    _direction, _magnitude = line.strip().split(" ")
    _magnitude = int(_magnitude)

    for _i in range(_magnitude):
        if _direction == "R":
            head_loc[0] += 1   
        elif _direction == "L":
            head_loc[0] -= 1
        elif _direction == "U":
            head_loc[1] -= 1
        elif _direction == "D":
            head_loc[1] += 1

        x_diff = head_loc[0] - tail_loc[0]
        y_diff = head_loc[1] - tail_loc[1]

        if abs(x_diff) > 1 and y_diff == 0:
            tail_loc[0] += x_diff/abs(x_diff)
        elif abs(y_diff) > 1 and x_diff == 0:
            tail_loc[1] += y_diff/abs(y_diff)
        elif abs(x_diff) == 1 and abs(y_diff) == 1:
            pass
        elif abs(x_diff) >= 1 and abs(y_diff) >= 1:
            if _direction == 'R':
                tail_loc[0] = head_loc[0] - 1
                tail_loc[1] = head_loc[1]
            elif _direction == 'L':
                tail_loc[0] = head_loc[0] + 1
                tail_loc[1] = head_loc[1]
            elif _direction == 'U':
                tail_loc[0] = head_loc[0]
                tail_loc[1] = head_loc[1] + 1
            elif _direction == 'D':
                tail_loc[0] = head_loc[0]
                tail_loc[1] = head_loc[1] - 1

        #print(f"Dir: {_direction}, Mag: {_magnitude},  Head ({head_loc[0]},{head_loc[1]}),  Tail ({tail_loc[0]},{tail_loc[1]})")
        locs_visited.add((tail_loc[0], tail_loc[1]))


# 10045 too high
print(len(locs_visited))