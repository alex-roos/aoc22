import FileTree

file = open("day_07_input.txt", "r")
data = file.read().strip().split("\n")
file.close()

tree = FileTree.Tree()
cmd_state = ""

for line in data:
    tokens = line.split(" ")
    if line[0] == '$':
        cmd_state = tokens[1]
        if cmd_state == "cd":
            dest_dir = tokens[2]
            tree.updateCurrDirectory(dest_dir)

    elif cmd_state == "ls":
        #print(f"Item {line} in folder {dir_state[-1]}")

        if tokens[0] == "dir":
            #print(f"Adding {tokens[1]} to {tree.curr_dir_state[-1].name} {tree.curr_dir_state[-1]}")
            tree.addNode(tokens[1], tree.curr_dir_state[-1], 0, "dir")
        else:
            tree.addNode(tokens[1], tree.curr_dir_state[-1], int(tokens[0]), "file")

#tree.populateDirSizes()

dir_size_list = [_x.size for _x in tree.dirs_list]
dir_size_list.sort()
#print(dir_size_list)

small_dirs_size = 0

free_space = 70000000 - tree.root.size
UNUSED_SPACE_OBJ = 30000000

for _s in dir_size_list:
    if free_space + _s >= UNUSED_SPACE_OBJ:
        print(_s)
        break

# for _s in dir_size_list:
#     print(f"size: {_s}")
#     if 70000000 - _s <= 30000000:
#         print(_s)
#         break


# 40389918 is too high
# print(small_dirs_size)