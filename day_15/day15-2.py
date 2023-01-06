global GLOBAL_ROWS, MAX_VALUE, SENSOR_ARRAY
MAX_VALUE = 20
GLOBAL_ROW = [0] * (MAX_VALUE + 1)

# 0: x, 1: y, 2: range
SENSOR_ARRAY = []

class Sensor:
    x = int()
    y = None

    beacon_x = int()
    beacon_y = int()

    min_row_reached = int()
    max_row_reached = int()

    dist_covered = int()

    def __init__(self, _s_x, _s_y, _b_x, _b_y) -> None:
        self.x = _s_x
        self.y = _s_y
        self.beacon_x = _b_x
        self.beacon_y = _b_y

        self.dist_covered = abs(_s_x-_b_x) + abs(_s_y - _b_y)

        self.min_row_reached = self.y - self.dist_covered
        self.max_row_reached = self.y + self.dist_covered

    def determineCoverage(self, concerned_row) -> None:
        global GLOBAL_ROW

        #print(f"----- Sensor: [{self.x},{self.y}] ------")

        # look ONLY at ONE ROW
        _remaining_dist = self.dist_covered - abs(self.y - concerned_row)
        if _remaining_dist > 0:
            row_x_start = self.x - _remaining_dist
            if row_x_start < 0:
                row_x_start = 0
            row_x_end = self.x + _remaining_dist
            if row_x_end > MAX_VALUE:
                row_x_end = MAX_VALUE

            for _x in range(row_x_start, row_x_end+1):
                GLOBAL_ROW[_x] = 1

file = open(r"C:\Users\ARoos\dev\git\aoc22\day_15\day_15_input_test.txt", "r")
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

    sensor_list.append(Sensor(_sensor_x, _sensor_y, _beacon_x, _beacon_y))

row_id = 0
found_incomplete_row = False

empty_x = -1
empty_y = -1

while not found_incomplete_row and row_id <= MAX_VALUE:
    GLOBAL_ROW = [0] * (MAX_VALUE + 1)

    for _sensor in sensor_list:
        _sensor.determineCoverage(row_id)
        # if _sensor.y == 11:
        #     print(GLOBAL_ROW)

    # if row_id % 100000 == 0:
    #     print(f"Row {row_id}: sum = {sum(GLOBAL_ROW)}")

    if sum(GLOBAL_ROW) != MAX_VALUE + 1:
        found_incomplete_row = True
        print(f"Found incomplete row # {row_id}.")
        empty_y = row_id

    row_id += 1

for _i in range(len(GLOBAL_ROW)):
    if GLOBAL_ROW[_i] == 0:
        empty_x = _i

print(f"Opening at x: {empty_x}, y: {empty_y}")