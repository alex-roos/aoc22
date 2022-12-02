file = open("day_02_input.txt", "r")
data = file.read().strip().split("\n")

play_points = {'X':1, 'Y':2, 'Z':3}

total = 0

for line in data: 
    opponent_play, my_play = line.split(" ")

    outcome = 0
    # A, X = Rock
    # B, Y = Paper
    # C, Z = Scissors
    if opponent_play == "A":
        if my_play == "X":
            outcome = 3
        elif my_play == "Y":
            outcome = 6
        else:
            outcome = 0
    elif opponent_play == "B":
        if my_play == "X":
            outcome = 0
        elif my_play == "Y":
            outcome = 3
        else:
            outcome = 6
    elif opponent_play == "C":
        if my_play == "X":
            outcome = 6
        elif my_play == "Y":
            outcome = 0
        else: 
            outcome = 3

    round_score = outcome + play_points[my_play]

    total += round_score

print(f"Points: {total}")

file.close()