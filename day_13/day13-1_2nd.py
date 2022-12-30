class PacketPair:
    class PacketNode:
        prev_node = None
        next_node = None
        contents = None

        def __init__(self, _prev, _next=None, _contents=None) -> None:
            self.prev_node = _prev
            self.next_node = _next

            if _contents != None:
                if type(_contents) == int:
                    self.contents = _contents
                elif type(_contents) == list:
                    self.contents = []
                    for _x in _contents:
                        self.contents.append(_x)

        def setContents(self, _item):
            if type(_item) == int:
                self.contents = _item
            elif type(_item) == list:
                self.contents = []
                for _x in _item:
                    self.contents.append(_x)

        def addToContentList(self, _item):
            if self.contents == None:
                self.contents = []

            self.contents.append(_item)

        def setNextNode(self, _next):
            self.next_node = _next

        def compareToRight(self, right_node):
            pass

        def hasNextNode(self):
            return self.next_node != None

    id = None
    packet_1 = []
    packet_2 = []

    def __init__(self, _id) -> None:
        self.packet_1 = []
        self.packet_2 = []
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
        if len(self.packet_1) < len(self.packet_2):
            return True
        elif len(self.packet_1) > len(self.packet_2):
            return False
        else:
            for idx in range(len(self.packet_1)):
                _next_item_1 = self.packet_1[idx]
                _next_item_2 = self.packet_2[idx]

                print(f"Comparing {_next_item_1} to {_next_item_2}")

                if type(_next_item_1) == int and type(_next_item_2) == int:
                    if _next_item_1 > _next_item_2:
                        return False
                elif type(_next_item_1) == list and type(_next_item_2) == list:
                    print(f"Both lists {_next_item_1} and {_next_item_2}")
            
            return True

    def __str__(self):
        return str(self.packet_1) + " AND " + str(self.packet_2)

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
    print(f"=========== Pair {_p.id} =========== {_p}")
    #print(f"Pair {_p.id} right order is {_p.comparePackets()}")
    
    print("*"*100)