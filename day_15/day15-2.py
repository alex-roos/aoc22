global GLOBAL_ROWS, MAX_VALUE
MAX_VALUE = 4000000
GLOBAL_ROWS = [[-1] for _ in range(MAX_VALUE+1)]

class Sensor:
    x = None
    y = None

    beacon_x = None
    beacon_y = None

    dist_covered = None

    def __init__(self, _s_x, _s_y, _b_x, _b_y) -> None:
        self.x = _s_x
        self.y = _s_y
        self.beacon_x = _b_x
        self.beacon_y = _b_y

        self.dist_covered = abs(_s_x-_b_x) + abs(_s_y - _b_y)
        self.determineCoverage()

    def determineCoverage(self) -> None:
        global GLOBAL_ROWS

        self.locs_covered = set()

        print(f"----- Sensor: [{self.x},{self.y}] ------")

        for _y_row in range(self.y - self.dist_covered, self.y + self.dist_covered + 1):
            if self.x == 1557973 and _y_row > 2708300 and _y_row % 10 == 0:
                print(_y_row)
                print(GLOBAL_ROWS[_y_row-1])
            if _y_row >= 0 and _y_row <= MAX_VALUE:
                _remaining_dist = self.dist_covered - abs(self.y - _y_row)
                row_x_start = self.x - _remaining_dist
                if row_x_start < 0:
                    row_x_start = 0
                row_x_end = self.x + _remaining_dist
                if row_x_end > MAX_VALUE:
                    row_x_end = MAX_VALUE

                if type(GLOBAL_ROWS[_y_row][0]) == int:
                    # no info yet for this row
                    GLOBAL_ROWS[_y_row] = [[row_x_start, row_x_end]]
                else:

                    GLOBAL_ROWS[_y_row].sort()

                    _temp_line_seg = [0] * (MAX_VALUE + 1)
                    for _i in range(row_x_start, row_x_end+1):
                        _temp_line_seg[_i] = 1

                    for _segment in GLOBAL_ROWS[_y_row]:
                        for _i in range(_segment[0], _segment[1]+1):
                            _temp_line_seg[_i] = 1

                    _segment_list = []

                    parse_state = "looking"

                    curr_x_start = -1

                    for _i in range(len(_temp_line_seg)):
                        if parse_state == "looking":
                            if _temp_line_seg[_i] == 1:
                                curr_x_start = _i
                                parse_state = "online"
                        elif parse_state == "online":
                            if _temp_line_seg[_i] == 0:
                                _segment_list.append([curr_x_start, _i-1])
                                parse_state = "looking"
                                curr_x_start = -1

                    if parse_state == "online":
                        _segment_list.append([curr_x_start,MAX_VALUE])

                    GLOBAL_ROWS[_y_row] = _segment_list

                #print(f"\tRow {_y_row}: from {row_x_start} to {row_x_end}")

file = open(r"C:\Users\ARoos\dev\git\aoc22\day_15\day_15_input.txt", "r")
data = file.read().strip().split("\n")
file.close()

sensor_list = []

combined_coverage = set()

for line in data:
    tokens = line.split('=')
    _sensor_x = int(tokens[1].split(',')[0])
    _sensor_y = int(tokens[2].split(':')[0])
    _beacon_x = int(tokens[3].split(',')[0])
    _beacon_y = int(tokens[4])

    _next_sensor = Sensor(_sensor_x, _sensor_y, _beacon_x, _beacon_y)


for _row in GLOBAL_ROWS:
    if len(_row) > 1:
        print(_row)