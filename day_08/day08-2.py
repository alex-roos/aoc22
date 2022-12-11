def treehouseScore(x_loc, y_loc, treehouse_height):
    _to_right_score = 0
    _to_left_score = 0
    _to_up_score = 0
    _to_down_score = 0

    # check to right
    for _col in range(x_loc+1, len(tree_heights[0])):
        _to_right_score += 1
        if tree_heights[y_loc][_col] >= treehouse_height:
            break            
    
    # check to left
    for _col in range(x_loc-1, -1, -1):
        _to_left_score += 1
        if tree_heights[y_loc][_col] >= treehouse_height:
            break

    for _row in range(y_loc+1, len(tree_heights)):
        _to_down_score += 1
        if tree_heights[_row][x_loc] >= treehouse_height:
            break            
    
    for _row in range(y_loc-1, -1, -1):
        _to_up_score += 1
        if tree_heights[_row][x_loc] >= treehouse_height:
            break            

    if (y_loc == 1 and x_loc == 2) or (y_loc == 3 and x_loc == 2):
        print(f"(row: {y_loc}, col: {x_loc})")
        print([_to_up_score, _to_left_score, _to_right_score, _to_down_score])

    return _to_right_score * _to_left_score * _to_up_score * _to_down_score

file = open("day_08_input.txt", "r")
data = file.read().strip().split("\n")
file.close()

tree_heights = []

for line in data:
    tree_heights.append([int(_x) for _x in line])

max_score = -1

for _row in range(1,len(tree_heights)-1):
    print(f"Checking row {_row+1}")
    for _col in range(1,len(tree_heights)-1):
        _s = treehouseScore(_col, _row, tree_heights[_row][_col])

        if (_row == 1 and _col == 2) or (_row == 3 and _col == 2):
            print(_s)

        if _s > max_score:
            max_score = _s

print(max_score)