file = open("day_05_input.txt", "r")
data = file.read().split("\n")
file.close()

parse_phase = 0  # 0=stack contents, 1=number of stacks, 2=blank line, 3 = instructions

stack_list = []
count_stacks = 0

# contains a tuple (count moved, from where, to where)
move_instructions = []

# Pass 1 - looking for count of stacks gathering move instructions
for line in data:
    if parse_phase == 0:
        if not '[' in line:
            parse_phase = 1

            # looking at stack numbers
            print(line.strip().split("  "))
            stack_IDs = [int(_x) for _x in line.strip().split("  ")]

            count_stacks = max(stack_IDs)

            parse_phase = 2
    if parse_phase == 2 and line == "":
        parse_phase = 3
    
    if parse_phase == 3 and line != "":
        count_moved = -1
        from_where = -1
        to_where = -1

        tokens = line.split(" ")

        token_id = 0  # 0=count moved, 1=from, 2=to
        for _t in tokens:
            if _t != "move" and _t != "from" and _t != "to" and _t != '':
                if token_id == 0:
                    count_moved = int(_t)
                    token_id+=1
                elif token_id == 1:
                    from_where = int(_t) - 1
                    token_id+=1
                elif token_id == 2:
                    to_where = int(_t) - 1
                    token_id+=1
        
        move_instructions.append((count_moved, from_where, to_where))

# create necessary stacks
for _i in range(count_stacks):
    stack_list.append([])


parse_phase = 0

for line in data:
    if parse_phase == 0 and '[' in line:
        for _stack_id in range(count_stacks):
            print("Stack parsing line" + line)
            _line_idx = 1+3*_stack_id+1*_stack_id
            if _line_idx < len(line):
                _token = line[1+3*_stack_id+1*_stack_id]

                if _token != ' ':
                    stack_list[_stack_id].append(_token)

        # tokens = line.split(' ')
        # print(tokens)
    else:
        parse_phase = 1
        break

print(stack_list)

for _i in range(len(stack_list)):
    stack_list[_i].reverse()

print(move_instructions)
print(stack_list)

for _instructions in move_instructions:
    count_moved = _instructions[0]
    from_where = _instructions[1]
    to_where = _instructions[2]

    print(f"Moving {count_moved} from {from_where} to {to_where}")
    for _i in range(count_moved):
        stack_list[to_where].append(stack_list[from_where].pop())
        print(f"Intermediate: {stack_list}")

print("FINAL RESULT")
print(stack_list)

for _i in range(len(stack_list)):
    print(stack_list[_i].pop(), end='')