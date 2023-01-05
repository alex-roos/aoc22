class PacketPair:
    id = None
    packet_1 = []
    packet_2 = []

    def __init__(self, _id) -> None:
        packet_1 = []
        packet_2 = []
        self.id = _id

    def isPacketDone(self, _pkt_id, _idx, _helper_stack):
        if _pkt_id == 1:
            _inspected_pkt = self.packet_1
        else:
            _inspected_pkt = self.packet_2 

        if (len(_inspected_pkt) == 0 or _idx > len(_inspected_pkt)-1) and len(_helper_stack) == 0:
            return True
        else:
            return False
    
    def isError(self):
        foundFaultyOrdering = False

        item_1 = self.packet_1.copy()
        item_2 = self.packet_2.copy()

        item_1_stack = []
        item_2_stack = []

        while not foundFaultyOrdering and (len(item_1) + len(item_1_stack) + len(item_2) + len(item_2_stack) != 0):
            #print(f"Stack One: {item_1_stack},\tStack Two: {item_2_stack}")

            # first check if there are any nested elements to compare
            if len(item_1_stack) != 0 or len(item_2_stack) != 0:
                
                # if left side runs out of items first, it's in the correct order
                if len(item_2_stack) == 0:
                    foundFaultyOrdering = True
                elif len(item_1_stack) == 0:
                    item_2_stack.pop()
                else:
                    if type(item_1_stack[-1]) == int and type(item_2_stack[-1]) == int:
                        if item_1_stack.pop() > item_2_stack.pop():
                            foundFaultyOrdering = True
                    elif type(item_1_stack[-1]) == list and type(item_2_stack[-1]) == list:
                        _list_1 = item_1_stack.pop()
                        _list_2 = item_2_stack.pop()

                        _list_1.reverse()
                        _list_2.reverse()

                        for _x in _list_1:
                            item_1_stack.append(_x)

                        for _x in _list_2:
                            item_2_stack.append(_x)
                    else:

                        if type(item_1_stack[-1]) == int:
                            _left_val = item_1_stack.pop()
                            _right_list = item_2_stack.pop()

                            while type(_right_list) == list and len(_right_list) > 0:
                                _right_list = _right_list.pop(0)

                            if  (type(_right_list) == int and _left_val > _right_list) or (type(_right_list) == list and len(_right_list) == 0):
                                foundFaultyOrdering = True

                            # // Solution if rules for mixed comparison extend beyond current element// 
                            # _left_val = item_1_stack.pop()
                            # item_1_stack.append([_left_val])
                        else:
                            _left_list = item_1_stack.pop()
                            _right_val = item_2_stack.pop()

                            while type(_left_list) == list and len(_left_list) > 0:
                                _left_list = _left_list.pop(0)

                            # print(f"Left List: {_left_list},\tRight Val: {_right_val}")

                            if type(_left_list) == int and _left_list > _right_val:
                                foundFaultyOrdering = True
                            
                            # // Solution if rules for mixed comparison extend beyond current element// 
                            # _right_val = item_2_stack.pop()
                            # item_2_stack.append([_right_val])
            else:
                if len(item_1) != 0 and len(item_2) != 0:
                    item_1_stack.append(item_1.pop(0))
                    item_2_stack.append(item_2.pop(0))
                else:
                    if len(item_2) == 0:
                        foundFaultyOrdering = True
                        item_1 = []
                    else:
                        item_2 = []

        return foundFaultyOrdering

    def __str__(self):
        return str(self.packet_1) + " - " + str(self.packet_2)

file = open("day_13_input.txt", "r")
data = file.read().strip().split("\n")
file.close()

packet_pair_list = []

parse_phase = "packet_one"
_next_pair = PacketPair(1)
packet_id = 1

for line in data:
    _building_list = []
    build_stack = []
    temp = []

    if parse_phase == "packet_one" or parse_phase == "packet_two":
        # parse out items of the list
        for _c in line:
            if _c == '[':
                build_stack.append([])
            elif _c == ']':
                temp = build_stack.pop()
                if len(build_stack) > 0:
                    build_stack[-1].append(temp)
                else:
                    _building_list.append(temp)

                temp = []
            elif _c != ',':
                if len(build_stack) == 0:
                    _building_list.append(int(_c))
                else:
                    build_stack[-1].append(int(_c))

        # move to the next phase of parsing
        if parse_phase == "packet_one":
            _next_pair.packet_1 = _building_list[0].copy()
            parse_phase = "packet_two"
        elif parse_phase == "packet_two":
            _next_pair.packet_2 = _building_list[0].copy()
            parse_phase = "new_line"

    elif parse_phase == "new_line":
        packet_pair_list.append(_next_pair)
        packet_id += 1
        _next_pair = PacketPair(packet_id)

        parse_phase = "packet_one"

packet_pair_list.append(_next_pair)

correct_sum = 0

for _p in packet_pair_list:
    if not _p.isError():
        correct_sum += _p.id
    #print(f"=========== Pair {_p.id} ===========")
    #print(f"Pair {_p.id} right order is {not _p.comparePackets()}")
    
    #print("*"*100)

# 552 was too low, 562 still too low
print(correct_sum)