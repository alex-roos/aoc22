class Sensor:
    x = None
    y = None

    beacon_x = None
    beacon_y = None

    dist_covered = None
    locs_covered = None

    concerned_row = None

    def __init__(self, _s_x, _s_y, _b_x, _b_y, _r) -> None:
        self.x = _s_x
        self.y = _s_y
        self.beacon_x = _b_x
        self.beacon_y = _b_y

        self.concerned_row = _r

        self.dist_covered = abs(_s_x-_b_x) + abs(_s_y - _b_y)
        self.determineCoverage()

    def determineCoverage(self) -> None:
        self.locs_covered = set()

        print(f"----- Sensor: [{self.x},{self.y}] ------")
        print(f"For row {self.concerned_row} the dist is {abs(self.y - self.concerned_row)} and beacon dist is {self.dist_covered}")

        if abs(self.y - self.concerned_row) <= self.dist_covered: 
            for _x_dist in range(self.dist_covered - abs(self.y - self.concerned_row) + 1):
                if not (self.beacon_y == self.concerned_row and self.beacon_x == self.x + _x_dist):
                    self.locs_covered.add((self.x + _x_dist, self.concerned_row))
                if not (self.beacon_y == self.concerned_row and self.beacon_x == self.x - _x_dist):
                    self.locs_covered.add((self.x - _x_dist, self.concerned_row))
                # self.locs_covered.add((self.x + _x_dist, self.y - _y_dist))
                # self.locs_covered.add((self.x - _x_dist, self.y - _y_dist))

file = open("day_15_input.txt", "r")
data = file.read().strip().split("\n")
file.close()

sensor_list = []

combined_coverage = set()
beacon_list = []

row_check = 2000000

for line in data:
    #print(line.split('='))

    tokens = line.split('=')
    _sensor_x = int(tokens[1].split(',')[0])
    _sensor_y = int(tokens[2].split(':')[0])
    _beacon_x = int(tokens[3].split(',')[0])
    _beacon_y = int(tokens[4])

    #print(f"sensor: [{_sensor_x}, {_sensor_y}]/ beacon: [{_beacon_x}, {_beacon_y}]")

    _next_sensor = Sensor(_sensor_x, _sensor_y, _beacon_x, _beacon_y, row_check)
    #beacon_list.append((_beacon_x, _beacon_y))

    sensor_list.append(_next_sensor)

    for _loc in _next_sensor.locs_covered:
        combined_coverage.add(_loc)

# for _s in sensor_list:
#     if _s.x == 8:
#         _temp = list(_s.locs_covered)
#         _temp.sort()
#         print(_temp)



position_count = 0
row_coverage = []

# for _loc in sensor_list:
#     print(f"[{_loc.x},{_loc.y}]")
#     if _loc.x == 12 and _loc.y == 14:
#         _t = list(_loc.locs_covered)
#         _t.sort()
#         print(_t)
    
#     combined_coverage.remove((_loc.beacon_x, _loc.beacon_y))

for _loc in combined_coverage:
    if _loc[1] == row_check:
        position_count += 1
        row_coverage.append(_loc)

print(f"{position_count}")

# row_coverage.sort()

# print(row_coverage)