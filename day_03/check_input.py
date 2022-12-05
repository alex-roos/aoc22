file_1 = open("input.txt", "r")
data_orig = file_1.read().strip().split("\n")
file_1.close()

file_2 = open("day_03_input.txt", "r")
data_direct = file_2.read().strip().split("\n")
file_2.close()

check_chars = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U', 'k', 'K', 'X', 'x', 'y', 'Y']

found_spec_chars = 0

for line in data_orig:
    for _c in check_chars:
        if _c in line:
            found_spec_chars += 1

print(found_spec_chars)

mismatch_lines = 0

for _idx in range(len(data_orig)):
    if not data_orig[_idx] == data_direct[_idx]:
        mismatch_lines += 1

print(f"Count mismatches: {mismatch_lines}")