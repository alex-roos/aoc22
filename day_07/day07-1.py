import FileTree

file = open("day_07_input.txt", "r")
data = file.read().strip().split("\n")
file.close()

tree = FileTree.Tree()

'''
DEBUG - START
'''
# tree.addNode("a", tree.root, 0, "dir")
# tree.addNode("d", tree.root, 0, "dir")
# print(f"Root is: {tree.root}")
# print([_x.name for _x in tree.dirs_list])
# tree.addNode("e", tree.getNode("a"), 0, "dir")
# tree.addNode("j", tree.getNode("d"), 0, "dir")
# print("+"*50 + "\n" + "+"*50)
# print(tree.getNode("e").name)
# print("="*50)
'''
DEBUG - END
'''

cmd_state = ""
dir_state = []

for line in data:
    tokens = line.split(" ")
    if line[0] == '$':
        cmd_state = tokens[1]
        if cmd_state == "cd":
            dest_dir = tokens[2]
            tree.updateCurrDirectory(dest_dir)

            # if dest_dir == "..":
            #     dir_state.pop()
            # else:
            #     dir_state.append(dest_dir)
    elif cmd_state == "ls":
        #print(f"Item {line} in folder {dir_state[-1]}")

        if tokens[0] == "dir":
            print(f"Adding {tokens[1]} to {tree.curr_dir_state[-1].name} {tree.curr_dir_state[-1]}")
            tree.addNode(tokens[1], tree.curr_dir_state[-1], 0, "dir")
        else:
            tree.addNode(tokens[1], tree.curr_dir_state[-1], int(tokens[0]), "file")

    #print(f"Dir state: {dir_state}")

tree.populateDirSizes()

small_dirs_size = 0

print(f"Root size is {tree.root.size}")
for _n in tree.dirs_list:
    if _n.size <= 100000:
        small_dirs_size += _n.size
    print(f"{_n.name}: {_n.size}")

# 142311 is too low
print(small_dirs_size)