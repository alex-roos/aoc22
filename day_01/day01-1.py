file = open("day_01_input.txt", "r")
data = file.read().strip().split("\n")

elfs = []

running_total = 0
for line in data:
    print(line)
    if line == "":
        elfs.append(running_total)
        running_total = 0
    else:
        running_total += int(line)
        print(line)

print(max(elfs))

file.close()