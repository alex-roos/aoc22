global GLOBAL_ROWS, MAX_VALUE, SENSOR_ARRAY
MAX_VALUE = 4000000
GLOBAL_ROW = [0] * (MAX_VALUE + 1)

# 0: x, 1: y, 2: range, 3: min_x_range, 4: max_x_range
SENSOR_ARRAY = []

file = open(r"C:\Users\ARoos\dev\git\aoc22\day_15\day_15_input.txt", "r")
data = file.read().strip().split("\n")
file.close()

for line in data:
    tokens = line.split('=')
    _sensor_x = int(tokens[1].split(',')[0])
    _sensor_y = int(tokens[2].split(':')[0])
    _beacon_x = int(tokens[3].split(',')[0])
    _beacon_y = int(tokens[4])

    SENSOR_ARRAY.append([_sensor_x, _sensor_y, abs(_sensor_x-_beacon_x) + abs(_sensor_y-_beacon_y)])

row_id = 0
found_incomplete_row = False

empty_x = -1
empty_y = -1

while not found_incomplete_row and row_id <= MAX_VALUE:
    segment_list = []

    for _sensor_info in SENSOR_ARRAY:
        _remaining_dist = _sensor_info[2] - abs(_sensor_info[1] - row_id)
        if _remaining_dist > 0:
            row_x_start = _sensor_info[0] - _remaining_dist
            if row_x_start < 0:
                row_x_start = 0
            row_x_end = _sensor_info[0] + _remaining_dist
            if row_x_end > MAX_VALUE:
                row_x_end = MAX_VALUE

            segment_list.append([row_x_start,row_x_end])
    
    segment_list.sort()
    if row_id % 100000 == 0:
        print(f"Row {row_id}")
        print(segment_list)
    #    print(f"Row {row_id}: sum = {sum(GLOBAL_ROW)}")

    _segment_id = 0
    max_right_limit = 0
    _line_is_complete = True

    while _line_is_complete and _segment_id < len(segment_list):

        if _segment_id == 0 and segment_list[_segment_id][0] != 0:
            _line_is_complete = False
        elif _segment_id == 0:
            max_right_limit = segment_list[_segment_id][1]
        else:
            if segment_list[_segment_id][0] > max_right_limit:
                _line_is_complete = False
            else:
                max_right_limit = max(max_right_limit, segment_list[_segment_id][1])
                empty_x = segment_list[_segment_id][1] + 1
            # if segment_list[_segment_id][1] < segment_list[_segment_id+1][0]:
            #     _line_is_complete = False

        if not _line_is_complete:
            found_incomplete_row = True
            print(f"Found incomplete row # {row_id}.")
            print(segment_list)
            empty_y = row_id

        _segment_id += 1

    row_id += 1



print(f"Opening at x: {empty_x}, y: {empty_y}")