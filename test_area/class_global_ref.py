GLOBAL_LIST = []

class ModList:

    inner_list = None

    def __init__(self, _l) -> None:
        self.inner_list = _l.copy()

        GLOBAL_LIST.append(self.inner_list)


for _i in range(10):
    ModList([_i,_i+1])

print(GLOBAL_LIST)