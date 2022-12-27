a = [[[[[]]]]]
b = []

i = 0 

while ((len(a) != 0 or len(b) != 0)):
    print(f"i:{i} has stack: {b}")

    if len(a) > 0:
        b.append(a.pop(0))
    else:
        if len(b[-1]) > 0:
            b.append(b[-1][0])
        else:
            b.pop(0)

    i += 1