file = open("day_10_input.txt", "r")
data = file.read().strip().split("\n")
file.close()

reg_x_val =  1
cycle = 1

sum = 0

for line in data:
    tokens = line.split(' ')
    if tokens[0] == "addx":
        _v = int(tokens[1])

        for _i in range(2):
            if cycle == 20 or ((cycle - 20) % 40) == 0:
                print(f"Cycle {cycle}: signal {reg_x_val*cycle} with  reg = {reg_x_val}")
                sum += reg_x_val*cycle

            cycle += 1
        
        reg_x_val += _v

    else:
        
        if cycle == 20 or ((cycle - 20) % 40) == 0:
            print(f"Cycle {cycle}: signal {reg_x_val*cycle} with  reg = {reg_x_val}")

            sum += cycle * reg_x_val

        cycle +=1

# 14911 too high
print(sum)