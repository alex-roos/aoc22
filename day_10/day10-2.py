file = open("day_10_input.txt", "r")
data = file.read().strip().split("\n")
file.close()

screen = []
screen_row =  -1

reg_x_val =  1
cycle = 1

sum = 0

for line in data:
    tokens = line.split(' ')

    ticks = 0
    _v = 0

    if tokens[0] == "addx":
        _v = int(tokens[1])
        ticks = 2
    else:
        ticks = 1

    for _i in range(ticks):
        if (cycle-1) % 40 == 0:
            screen_row += 1
            screen.append([])

        if reg_x_val-1 <= (cycle-1)%40 <= reg_x_val+1:
            _c = '#'
        else:
            _c = '.'

        screen[screen_row].append(_c)

        print(f"Cycle {cycle}: x->{reg_x_val}    drawing {_c}")

        if cycle == 20 or ((cycle - 20) % 40) == 0:
            print(f"Cycle {cycle}: signal {reg_x_val*cycle} with  reg = {reg_x_val}")
            sum += reg_x_val*cycle

        cycle += 1

    reg_x_val += _v  

print(sum)

for _i in range(len(screen)):
    for _j in screen[_i]:
        print(_j, end='')
    print()