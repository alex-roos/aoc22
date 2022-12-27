a = [1,[2,[3,[4,[5,6,7]]]],8,9]
b = [[[[]]]]

my_stack = []

to_add = a.copy()

while (len(to_add) > 0):
    print(f"Stack is: {my_stack} and to_add is: {to_add}")

    my_stack.append([])
    
    for _x in range(len(to_add)):
        if type(_x) == int:
            my_stack[-1].append(to_add.pop(0))
        else:
            to_add = to_add[0]
            break

my_stack.insert(0, to_add)

print(f"Stack is: {my_stack} and to_add is: {to_add}")