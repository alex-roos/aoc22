def findNeighbors(curr_row, curr_col, puzz_map, _visited):
    neighbor_locs = []
    map_width = len(puzz_map[0])
    map_height = len(puzz_map)

    #check up
    if curr_row > 0 and (curr_row-1, curr_col) not in _visited and abs(puzz_map[curr_row][curr_col] - puzz_map[curr_row-1][curr_col]) <= 1:
        neighbor_locs.append([curr_row-1, curr_col])

    #check down
    if curr_row < map_height-1 and (curr_row+1, curr_col) not in _visited and abs(puzz_map[curr_row][curr_col] - puzz_map[curr_row+1][curr_col]) <= 1:
        neighbor_locs.append([curr_row+1, curr_col])

    #check left
    if curr_col > 0 and (curr_row, curr_col-1) not in _visited and abs(puzz_map[curr_row][curr_col] - puzz_map[curr_row][curr_col-1]) <= 1:
        neighbor_locs.append([curr_row, curr_col-1])

    #check right
    if curr_col < map_width - 1 and (curr_row, curr_col+1) not in _visited and abs(puzz_map[curr_row][curr_col] - puzz_map[curr_row][curr_col+1]) <= 1:
        neighbor_locs.append([curr_row, curr_col+1])

    return neighbor_locs

WIDTH = 143
HEIGHT = 41

file = open("day_12_input.txt", "r")
data = file.read().strip().split("\n")
file.close()

start_loc = (20,0)
end_loc = (20,121)
curr_node = start_loc
visited = set()
unvisited = set()

for _r in range(HEIGHT):
    for _c in range(WIDTH):
        unvisited.add((_r, _c))

puzzle_map = []
distance_values = [ [float("inf")] * WIDTH for _ in range(HEIGHT)]
distance_values[start_loc[0]][start_loc[1]] = 0
neighbor_counts = [ ['X'] * WIDTH for _ in range(HEIGHT)]

original_input = []

for line in data:
    _next_line = []
    _orig_next_line = []
    for _c in line:
        _orig_next_line.append(_c)
        if _c == 'S':
            _next_line.append(ord('a'))
        elif _c == 'E':
            _next_line.append(ord('z'))
        else:
            _next_line.append(ord(_c))
    
    original_input.append(_orig_next_line)
    puzzle_map.append(_next_line)

# kick start by exploring from start node
for _neighbors in findNeighbors(start_loc[0], start_loc[1], puzzle_map, visited):
    if distance_values[curr_node[0]][curr_node[1]] + 1 < distance_values[_neighbors[0]][_neighbors[1]]:
        distance_values[_neighbors[0]][_neighbors[1]] = distance_values[curr_node[0]][curr_node[1]] + 1

while end_loc not in visited:
    min_dist = float("inf")

    for _row in range(HEIGHT):
        for _col in range(WIDTH):
            if (_row, _col) not in visited and distance_values[_row][_col] <= min_dist:
                min_dist = distance_values[_row][_col]
                curr_node = (_row, _col)

    curr_node_neighbors = findNeighbors(curr_node[0], curr_node[1], puzzle_map, visited)
    neighbor_counts[curr_node[0]][curr_node[1]] = len(curr_node_neighbors)

    for _neighbors in curr_node_neighbors:
        if distance_values[curr_node[0]][curr_node[1]] + 1 < distance_values[_neighbors[0]][_neighbors[1]]:
            distance_values[_neighbors[0]][_neighbors[1]] = distance_values[curr_node[0]][curr_node[1]] + 1
    
    print(f"Visited Node: {curr_node} with dist {min_dist} and neighbors {curr_node_neighbors}.")
    visited.add(curr_node)

# for row in distance_values:
#     for _x in row:
#         print(_x, end='  ')
#     print()

#print(findNeighbors(0,2,puzzle_map, visited))
print(f"Value at end = {distance_values[end_loc[0]][end_loc[1]]}")

neighbor_ct_file = open("neighbors_found.txt", "w")

for _row in neighbor_counts:
    for _ct in _row:
        neighbor_ct_file.write(str(_ct))
    neighbor_ct_file.write('\n')

neighbor_ct_file.close()

visited_file = open("visited_found.txt", "w")

for _row_idx in range(HEIGHT):
    for _col_idx in range(WIDTH):
        if neighbor_counts[_row_idx][_col_idx] != 'X':
            visited_file.write(original_input[_row_idx][_col_idx])
        else:
            visited_file.write('X')
    visited_file.write('\n')

visited_file.close()