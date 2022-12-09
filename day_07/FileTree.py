class Node:
    def __init__(self, _name, _parent, _size, _type):
        self.children = []
        self.parent = _parent
        self.name = _name
        self.size = _size
        self.type = _type

class Tree:
    root = None
    dirs_list = []
    #unique_name_dict = dict()

    curr_dir_state = []

    def __init__(self):
        self.root = Node("/", None, 0, "dir")
        self.curr_dir_state = [self.root]

    def updateCurrDirectory(self, dirChange):
        if dirChange == "/":
            self.curr_dir_state = [self.root]
        elif dirChange == "..":
            self.curr_dir_state.pop()
        else:
            next_dir = None
            for _c in self.curr_dir_state[-1].children:
                if dirChange == _c.name:
                    next_dir = _c
            self.curr_dir_state.append(next_dir)
    
    def addNode(self, name, parent, size, type):
        # print(f"Parent name: {parent.name}")
        # if name in self.unique_name_dict.keys():
        #     print(f"Duplicate Name: {name}")
        #     name = name + "_" + str(self.unique_name_dict[name])
        #     print(f"New name: {name}")

        #     self.unique_name_dict[name] += 1
        # else:
        #     self.unique_name_dict[name] = 1

        # if name in [_x.name for _x in self.dirs_list]:
        #     print(self.unique_name_dict)
        
        newNode = Node(name, parent, size, type)
        parent.children.append(newNode)

        if type == "dir":
            self.dirs_list.append(newNode)
        elif type == "file":
            _update_dir = parent

            while _update_dir.name != '/':
                _update_dir.size += size
                _update_dir = _update_dir.parent
            
            self.root.size += size

    # def getNode(self, name):
    #     if name == "/":
    #         return self.root
    #     else:
    #         return self.NodeSearchHelper(self.root, name)

    # # this whole function could be replaced with a map....
    # def NodeSearchHelper(self, _n, search_name):
    #     names = [_x.name for _x in _n.children]

    #     answer = set()
    #     answer.add(None)

    #     #print(f"Searching within {names} with _n {_n}")

    #     if search_name in names:
    #         for _c in _n.children:
    #             if search_name == _c.name:
    #                 #print(f"Found the name! [{_c.name}]")
    #                 return _c
    #     else:
    #         for _c in _n.children:
    #             answer.add(self.NodeSearchHelper(_c, search_name))
    #     #print(f"Ans to return: {answer}")
    #     if len(answer) > 1:
    #         distinct_answer = None
    #         for _i in answer:
    #             if _i != None:
    #                 distinct_answer = _i
    #         return distinct_answer
    #     else:
            
    #         return list(answer)[0]


    # UNNECESSARY - directory sizes are all updated as files are added
    def populateDirSizes(self):
        for _c in self.root.children:
            self.root.size += self.dirSizeHelper(_c)

    def dirSizeHelper(self, curr_node):
        curr_size = 0

        if curr_node.type == "file":
            return curr_node.size
        else:
            print(f"Node {curr_node.name} has children {[_x.name for _x in curr_node.children]}")
            for _c in curr_node.children:

                if _c.type == "file":
                    curr_size += _c.size
                elif _c.type == "dir":
                    curr_size += self.dirSizeHelper(_c)

            curr_node.size = curr_size

            #print(f"Found size {curr_size} for node {curr_node.name}.")

            return curr_size