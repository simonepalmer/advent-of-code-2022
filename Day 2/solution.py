# Advent of code 2022
# Day 2

# Part one
# How many total points after doing all rounds according to the strategy guide?

# Part two
# How many total points after doing all rounds but the second column says how the
# round needs to end: X mean I need to lose, Y means it needs to end in a draw and Z
# means that I need to win

# Rock, paper, scissors /w strategy guide!
# chosing rock      =        1 point
# chosing paper     =        2 points
# chosing scissors  =        3 points
# loss              =        0 points
# draw              =        3 points
# win               =        6 points

# Test input series, A-C opponent choice, X-Z your choice:
# A Y
# B X
# C Z

# A, X, rock
# B, Y, paper
# C, Z, scissors

# A X - 4
# A Y - 8
# A Z - 3
# B X - 1
# B Y - 5
# B Z - 9
# C X - 7
# C Y - 2
# C Z - 6

def import_and_format_data():
    data = open("input.txt")
    data = data.read()
    strategy_guide = data.split('\n')
    return strategy_guide

# This is super ugly but I think it works... 
# I will try to get back to this later and see if I can improve it
def score_rounds_part_one(strategy_guide): # Part one score
    score_p1 = 0
    for round in strategy_guide:
        if 'X' in round:
            score_p1 += 4 # 1 for rock & 3 for draw
            if 'C' in round:
                score_p1 += 3 # +3 if win
            elif 'B' in round:
                score_p1 -= 3 # -3 if lose
        elif 'Y' in round:
            score_p1 += 5
            if 'A' in round:
                score_p1 += 3
            elif 'C' in round:
                score_p1 -= 3
        elif 'Z' in round:
            score_p1 += 6
            if 'B' in round:
                score_p1 += 3
            elif 'A' in round:
                score_p1 -= 3
    return score_p1

# This is even uglier than part 1, I will really need to find a proper way to do this
def score_rounds_part_two(strategy_guide):
    score_p2 = 0
    for round in strategy_guide:
        if 'X' in round: # need to lose (only points for sign)
            if 'A' in round:
                score_p2 += 3
            elif 'B' in round:
                score_p2 += 1
            else: # 'C'
                score_p2 += 2
        if 'Y' in round: # needs to end in draw 
            if 'A' in round:
                score_p2 += 4
            elif 'B' in round:
                score_p2 += 5
            else: # 'C'
                score_p2 += 6
        if 'Z' in round: # need to win
            if 'A' in round:
                score_p2 += 8
            elif 'B' in round:
                score_p2 += 9
            else: #'C'
                score_p2 += 7
    return score_p2

def print_total_score(score_p1, score_p2):
    print(score_p1) #12276
    print(score_p2) #9975

def main():
    strategy_guide = import_and_format_data()
    score_p1 = score_rounds_part_one(strategy_guide)
    score_p2 = score_rounds_part_two(strategy_guide)
    print_total_score(score_p1, score_p2)

if __name__ == "__main__":
    main()

