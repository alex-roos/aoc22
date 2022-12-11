file = open("day_08_input.txt", "r")
data = file.read().strip().split("\n")
file.close()

tree_heights = []
# NOTE: [ [0] * len(data)] * len(data) creates a 2d array but each row references the same list object
vis_matrix = [ [0] * len(data) for _ in range(len(data))]

for _row in range(len(vis_matrix)):
    for _col in range(len(vis_matrix)):
        if _row == 0 or _row == (len(vis_matrix) - 1):
            vis_matrix[_row][_col] = 1
        elif _col == 0 or _col == len(vis_matrix) - 1:
            vis_matrix[_row][_col] = 1

for line in data:
    tree_heights.append([int(_x) for _x in line])

print("Checking left to right")
# check left to right
for _row in range(1, len(tree_heights)-1):
    _max_height = tree_heights[_row][0]
    for _col in range(1, len(tree_heights[0])-1):
        if tree_heights[_row][_col] > _max_height:
            _max_height = tree_heights[_row][_col]
            vis_matrix[_row][_col] = 1

print("Checking right to left")
# check right to left
for _row in range(1, len(tree_heights)-1):
    _max_height = tree_heights[_row][-1]
    for _col in range(len(tree_heights[0])-1, 0, -1):
        if tree_heights[_row][_col] > _max_height:
            _max_height = tree_heights[_row][_col]
            vis_matrix[_row][_col] = 2

print("Checking up to down")
# check up to down
for _col in range(1, len(tree_heights)-1):
    _max_height = tree_heights[0][_col]
    for _row in range(1,len(tree_heights[0])-1):
        if tree_heights[_row][_col] > _max_height:
            _max_height = tree_heights[_row][_col]
            vis_matrix[_row][_col] = 3

print("Checking down to up")
# check down to up
for _col in range(1, len(tree_heights) - 1):
    _max_height = tree_heights[-1][_col]
    for _row in range(len(tree_heights[0])-1, 0, -1):
        if tree_heights[_row][_col] > _max_height:
            _max_height = tree_heights[_row][_col]
            vis_matrix[_row][_col] = 4

print(vis_matrix)
sum = 0
for _row in vis_matrix:
    for _i in _row:
        if _i != 0:
            sum += 1

# 2187, 2007 is too high
print(sum)