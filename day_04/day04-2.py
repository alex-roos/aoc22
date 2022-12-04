file = open("day_04_input.txt", "r")
data = file.read().strip().split("\n")
file.close()

#write_file = open("day04_output.txt", "a")

elf_pairs = []

for line in data:
    unparsed_elf_1, unparsed_elf_2 = line.split(',')

    elf_pairs.append([([int(_x) for _x in unparsed_elf_1.split('-')]), ([int(_x) for _x in unparsed_elf_2.split('-')])])

count_overlaps = 0

line_no = 1

for pair in elf_pairs:
    prev_count_overlaps = count_overlaps

    elf1_sect_start, elf1_sect_end = pair[0]
    elf2_sect_start, elf2_sect_end = pair[1]

    output_array_1 = 100 * ['--']
    output_array_2 = 100 * ['--']

    found_an_overlap = False

    for _i in range(elf1_sect_start, elf1_sect_end):
        if _i > 9:
            output_array_1[_i] = str(_i)
        else:
            output_array_1[_i] = "0" + str(_i)

    for _i in range(elf2_sect_start, elf2_sect_end):
        if _i > 9:
            output_array_2[_i] = str(_i)
        else:
            output_array_2[_i] = "0" + str(_i)

    if elf1_sect_start <= elf2_sect_start:
        if elf1_sect_end >= elf2_sect_end:
            count_overlaps += 1
            print(pair)
            found_an_overlap = True
    
    if not found_an_overlap and (elf2_sect_start <= elf1_sect_start):
        if elf2_sect_end >= elf1_sect_end:
            count_overlaps += 1
            print(pair)
            found_an_overlap = True

    if not found_an_overlap and (elf1_sect_start >= elf2_sect_start and elf1_sect_start <= elf2_sect_end):
        count_overlaps += 1
        print(f"Case 3: {pair}")
        found_an_overlap = True

    if not found_an_overlap and (elf1_sect_end >= elf2_sect_start and elf1_sect_end <= elf2_sect_end):
        count_overlaps += 1
        print(f"Case 4: {pair}")
        found_an_overlap = True

    # if prev_count_overlaps ==count_overlaps:
    #     write_file.write(f"Line {line_no} for {pair}\n")
    #     write_file.write(' '.join(output_array_1))
    #     write_file.write("\n")  
    #     write_file.write(' '.join(output_array_2))
    #     write_file.write("\n")

    line_no += 1


# 416 too low, 511 too high
print(f"Total full contains: {count_overlaps}")

#write_file.close()