file = open("day_09_input_test.txt", "r")
data = file.read().strip().split("\n")
file.close()

def printBoard(_curr_state, _head_loc):
    _curr_board = [ ['.'] * 6 for _ in range(5)]

    _rope_idx = 1
    
    for _coord in _curr_state:
        _curr_board[_coord[1]+4][_coord[0]] = str(_rope_idx)

        _rope_idx += 1

    #print(f"Adding Head: x={_head_loc[1]+4}, y={_head_loc[0]}")
    _curr_board[_head_loc[1]+4][_head_loc[0]] = 'H'

    for _row in range(5):
        for _col in range(6):
            print(_curr_board[_row][_col], end='')
        print()


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

ropes_loc = [[0,0] for _ in range(9)]

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

        for _rope_idx in range(9):

            move_str = "UNK"

            x_diff = 0
            y_diff = 0

            if _rope_idx == 0:
                x_diff = head_loc[0] - ropes_loc[0][0]
                y_diff = head_loc[1] - ropes_loc[0][1]
            else:
                x_diff = ropes_loc[_rope_idx-1][0] - ropes_loc[_rope_idx][0]
                y_diff = ropes_loc[_rope_idx-1][1] - ropes_loc[_rope_idx][1]

            if abs(x_diff) > 1 and y_diff == 0:
                ropes_loc[_rope_idx][0] += int(x_diff/abs(x_diff))
                move_str = "horizontal"
            elif abs(y_diff) > 1 and x_diff == 0:
                ropes_loc[_rope_idx][1] += int(y_diff/abs(y_diff))
                move_str = "vertical"
            elif (abs(x_diff) == 1 and abs(y_diff) == 1) or (x_diff == 0 and y_diff == 0):
                move_str = "unchanged"
            elif abs(x_diff) >= 1 and abs(y_diff) >= 1:
                lead_node = [-20,-20]
                if _rope_idx == 0:
                    lead_node = head_loc
                else:
                    lead_node = ropes_loc[_rope_idx-1]

                if _direction == 'R':
                    ropes_loc[_rope_idx][0] = lead_node[0] - 1
                    ropes_loc[_rope_idx][1] = lead_node[1]
                elif _direction == 'L':
                    ropes_loc[_rope_idx][0] = lead_node[0] + 1
                    ropes_loc[_rope_idx][1] = lead_node[1]
                elif _direction == 'U':
                    ropes_loc[_rope_idx][0] = lead_node[0]
                    ropes_loc[_rope_idx][1] = lead_node[1] + 1
                elif _direction == 'D':
                    ropes_loc[_rope_idx][0] = lead_node[0]
                    ropes_loc[_rope_idx][1] = lead_node[1] - 1
                
                move_str = "diagonal"

            #print(f"Dir: {_direction}, Mag: {_magnitude},  Head ({head_loc[0]},{head_loc[1]}),  Tail ({tail_loc[0]},{tail_loc[1]})")
            if _rope_idx == 0:
                lead_node = head_loc
            else:
                lead_node = ropes_loc[_rope_idx-1]
            print(f"Lead node: (x={lead_node[0]},y={lead_node[1]}), Rope {_rope_idx+1}: (x={ropes_loc[_rope_idx][0]},y={ropes_loc[_rope_idx][1]}) with move type {move_str}")
            
            locs_visited.add((ropes_loc[_rope_idx][0], ropes_loc[_rope_idx][1]))
        print("@"*50)
        printBoard(ropes_loc, head_loc)

print(len(locs_visited))