def remainingElements(_val_1, _val_1_stack, _val_2, _val_2_stack):
    return len(_val_1) + len(_val_1_stack) + len(_val_2) + len(_val_2_stack) != 0

a = [[[[[]]]]]
b = []

i = 0 

while ((len(a) != 0 or len(b) != 0)):
    #print(f"i:{i} has stack: {b}")

    if len(a) > 0:
        b.append(a.pop(0))
    else:
        if len(b[-1]) > 0:
            b.append(b[-1][0])
        else:
            b.pop(0)

    i += 1


item_1 = [[5,[[3,0]],[0,[8,6,9],2,9],[5,6,[2,8,3],[0]],[6,2,[2,6,8],10]]]
item_2 = [[6,4,[2,[2,2],8,[3,7,0,6,2]]],[4,10]]

item_1_stack = []
item_2_stack = []

foundFaultyOrdering = False

while not foundFaultyOrdering and remainingElements(item_1, item_1_stack, item_2, item_1_stack):
    print(f"Stack One: {item_1_stack},\tStack Two: {item_2_stack}")

    # first check if there are any nested elements to compare
    if len(item_1_stack) != 0 or len(item_2_stack) != 0:
        
        # if left side runs out of items first, it's in the correct order
        if len(item_2_stack) == 0:
            foundFaultyOrdering = True
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
                    #_right_list = item_2_stack.pop()

                    # if _left_val > _right_list[0]:
                    #     foundFaultyOrdering = True

                    item_1_stack.append([_left_val])
                else:
                    #_left_list = item_1_stack.pop()
                    _right_val = item_2_stack.pop()

                    # if _left_list[0] > _right_val:
                    #     foundFaultyOrdering = True
                    item_2_stack.append([_right_val])

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

if not foundFaultyOrdering:
    print("Everything in order.")
else:
    print(f"ERROR in ordering. Stack state: {item_1_stack}, {item_2_stack}")