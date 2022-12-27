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
    
    def comparePackets(self):
        right_order = True
        has_more_items = True

        inspection_idx = 0

        packet_one_stack = []
        packet_two_stack = []

        while(has_more_items):
            print(f"P1[{inspection_idx}], P2[{inspection_idx}]", end='')

            pkt_one_done = self.isPacketDone(1, inspection_idx, packet_one_stack)
            pkt_two_done = self.isPacketDone(2, inspection_idx, packet_two_stack)

            if pkt_one_done or pkt_two_done:
                if pkt_two_done and not pkt_one_done:
                    return False
                else:
                    return True
            else:  # guaranteed at least one item in their stack or list
                _next_item_1 = []
                _next_item_2 = []

                working_off_stack_one = False
                working_off_stack_two = False

                # if len(packet_one_stack) == 0:
                #     _next_item_1 = self.packet_1[inspection_idx]
                #     inspection_idx += 1
                # else:
                #     _next_item_1 = packet_one_stack.pop()
                #     working_off_stack_one = True

                # if len(packet_two_stack) == 0:
                #     _next_item_2 = self.packet_2[inspection_idx]
                #     inspection_idx += 1
                # else:
                #     _next_item_2 = packet_two_stack.pop()
                #     working_off_stack_two = True

                if len(packet_one_stack) > 0 or len(packet_two_stack) > 0:
                    _next_item_1 = packet_one_stack.pop()
                    _next_item_2 = packet_two_stack.pop()
                    

                print(f"\tComparing Items: {_next_item_1} and {_next_item_2}")

                
                if type(_next_item_1) == int and type(_next_item_2) == int:
                    if _next_item_1 > _next_item_2:
                        return False
                elif type(_next_item_1) == list and type(_next_item_2) == list:
                    print(f"Both lists {_next_item_1} and {_next_item_2}")
                    print(f"Stacks are {packet_one_stack} && {packet_two_stack}")
                    if len(_next_item_1) == 0 or len(_next_item_2) == 0:
                        if len(_next_item_1) > len(_next_item_2):
                            return False
                        else:
                            inspection_idx += 1

                            packet_one_stack = []
                            packet_two_stack = []
                            print("KEEEEEPPPPPP GOING????")
                    else: 
                        # BOTH items are lists with AT LEAST ONE ITEM
                        # BUT we don't know if the items are from the base list or stack
                        # so let's throw those items on the stack and compare as usual
                        
                        print("Adding back to stacks")

                        if working_off_stack_one:
                            packet_one_stack.append(_next_item_1)

                        packet_one_stack.append(_next_item_1[0])
                        
                        if working_off_stack_two:
                            packet_two_stack.append(_next_item_2)

                        packet_two_stack.append(_next_item_2[0])

                        print(f"Appended stacks are {packet_one_stack} && {packet_two_stack}")


                else:  # mix of list and int
                    if type(_next_item_1) == list:
                        print(f"First item list, but not second: {_next_item_1}, {_next_item_2}")
                        # Need to try again, so need to figure out where to rewind packet 1, stack or index
                        if len(packet_one_stack) == 0:
                            inspection_idx -= 1
                        else:
                            packet_one_stack.append(_next_item_1) 
                        packet_two_stack.append([_next_item_2])
                    else:
                        print(f"Second item list, but not first: {_next_item_1}, {_next_item_2}")
                        if len(packet_two_stack) == 0:
                            inspection_idx -= 1
                        else:
                            packet_two_stack.append(_next_item_2)
                        packet_one_stack.append([_next_item_1])

            print()

        return right_order

    def __str__(self):
        return str(self.packet_1) + " - " + str(self.packet_2)

file = open("day_13_input_test.txt", "r")
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

for _p in packet_pair_list:
    print(f"=========== Pair {_p.id} ===========")
    print(f"Pair {_p.id} right order is {_p.comparePackets()}")
    
    print("*"*100)