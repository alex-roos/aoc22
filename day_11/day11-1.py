class Monkey:
    id = None
    items_queue = []
    operation = []
    mod_test_value = -1

    true_monkey = -1
    false_monkey = -1

    item_inspections = 0

    def __init__(self, _data_list) -> None:
        self.id = _data_list[0]

        self.items_queue = []
        for _i in _data_list[1]:
            self.items_queue.append(_i)
        
        self.operation = _data_list[2]
        self.mod_test_value = _data_list[3]

        self.true_monkey = _data_list[4]
        self.false_monkey = _data_list[5]

        self.item_inspections = 0

    def addItems(self, new_item):
        self.items_queue.append(new_item)
    
    def updateWorry(self):
        _return_values = []

        for _idx, _val in enumerate(self.items_queue):
            self.item_inspections += 1

            _old = _val
            if self.operation[0] == "old":
                operand_1 = _old
            else:
                operand_1 = int(self.operation[0])

            if self.operation[2] == "old":
                operand_2 = _old
            else:
                operand_2 = int(self.operation[2])            

            _result = None
            if self.operation[1] == '+':
                _result = operand_1 + operand_2
            elif self.operation[1] == '-':
                _result = operand_1 - operand_2
            elif self.operation[1] == "*":
                _result = operand_1 * operand_2

            _return_values.append(int(_result / 3))
            # print(f"\t\tWorried Level of {_old} now {_result}.")
            # self.items_queue[_idx] = int(_result / 3)
            # print(f"\t\tDecreased worry to {int(_result / 3)}.")
        self.items_queue = []
        return _return_values

    def runTurn(self):
        #print(f"Monkey {self.id}: {self.items_queue}")

        updated_items = self.updateWorry()

        thrown_items = []

        for _m in updated_items:
            if _m % self.mod_test_value == 0:
                thrown_items.append((self.true_monkey, _m))
            else:
                thrown_items.append((self.false_monkey, _m))

        return thrown_items

class MonkeyTree:
    monkey_list = []

    round_count = 1
    turn_count = 0

    def __init__(self) -> None:
        self.round_count = 1
        self.turn_count = 0
        self.monkey_list = []

    def addMonkey(self, _monkey_data_list):
        self.monkey_list.append(Monkey(_monkey_data_list))

    def runRound(self):
        for _m_idx in range(len(self.monkey_list)):
            aerial_items = []
            aerial_items = self.monkey_list[_m_idx].runTurn()

            #print(f"Thrown items: {aerial_items}")

            for _a in aerial_items:
                self.monkey_list[_a[0]].addItems(_a[1])

            self.turn_count += 1
        
        # print(f"######### ROUND {self.round_count} #########")
        # for _m in self.monkey_list:
        #     print(f"Monkey {_m.id}: {_m.items_queue}")

        self.turn_count = 0
        self.round_count += 1

file = open("day_11_input.txt", "r")
data = file.read().strip().split("\n")
file.close()

monkey_tree = MonkeyTree()

parse_phase = None
_curr_monkey_data = []

for line in data:
    if "Monkey" in line:
        #print(_curr_monkey_data)

        _curr_monkey_data = []
        parse_phase = "monkey_id"

        _curr_monkey_data.append(int(line[7]))

        parse_phase = "items"
    elif parse_phase == "items":
        tokens = line.strip().split(':')
        _vals = [int(_x) for _x in tokens[1].strip().split(',')]

        _curr_monkey_data.append(_vals)

        parse_phase = "operation"
    elif parse_phase == "operation":
        tokens = line.split("=")
        _ops = tokens[1].strip().split(' ')
        _curr_monkey_data.append(_ops)

        parse_phase = "test"
    elif parse_phase == "test":
        tokens = line.split(' ')

        _curr_monkey_data.append(int(tokens[-1]))
        
        parse_phase = "true_result"

    elif parse_phase == "true_result":
        _end = int(line[-1])
        _curr_monkey_data.append(_end)

        parse_phase = "false_result"

    elif parse_phase == "false_result":
        tokens = line.strip().split(' ')
        try:
            _curr_monkey_data.append(int(tokens[-1]))
        except:
            print(f"line: {line} has tokens: {tokens} at phase {parse_phase}")

        #print(f"Curr monkey data: {_curr_monkey_data}")
        monkey_tree.addMonkey(_curr_monkey_data)        

        parse_phase = "line_break"

    elif parse_phase == "line_break":
        pass

for i in range(20):
    monkey_tree.runRound()

inspection_list = []

for monkey in monkey_tree.monkey_list:
    print(f"Monkey {monkey.id} item count: {monkey.item_inspections}")
    inspection_list.append(monkey.item_inspections)

inspection_list.sort()

print(f"Monkey business: {inspection_list[-1] * inspection_list[-2]}")