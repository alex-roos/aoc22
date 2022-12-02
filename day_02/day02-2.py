file = open("day_02_input.txt", "r")
data = file.read().strip().split("\n")

play_points = {'X':0, 'Y':3, 'Z':6}

total = 0

for line in data: 
    opponent_play, result = line.split(" ")

    outcome = 0
    # A, X = Rock
    # B, Y = Paper
    # C, Z = Scissors
    if opponent_play == "A":
        if result == "X":
            outcome = 3
        elif result == "Y":
            outcome = 1
        else:
            outcome = 2
    elif opponent_play == "B":
        if result == "X":
            outcome = 1
        elif result == "Y":
            outcome = 2
        else:
            outcome = 3
    elif opponent_play == "C":
        if result == "X":
            outcome = 2
        elif result == "Y":
            outcome = 3
        else: 
            outcome = 1
    
    round_score = outcome + play_points[result]

    #print(f"Round: {round_score}")

    total += round_score

print(f"Points: {total}")

file.close()