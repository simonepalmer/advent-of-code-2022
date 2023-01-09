# Advent of code 2022
# Day 2

# Part one
# How many total points after doing all rounds according to the strategy guide?

# Part two
# How many total points after doing all rounds but the second column says how the
# round needs to end: X mean I need to lose, Y means it needs to end in a draw and Z
# means that I need to win

def import_and_format_data():
    data = open("input.txt")
    data = data.read()
    strategy_guide = data.split('\n')
    return strategy_guide

# Changed out a huge mess of nested if-statements to a score map
def score_rounds_part_one(strategy_guide): # Part one score
    score_map_part_one = {
        'A X': 4,
        'A Y': 8,
        'A Z': 3,
        'B X': 1,
        'B Y': 5,
        'B Z': 9,
        'C X': 7,
        'C Y': 2,
        'C Z': 6,
    }
    score_p1 = 0
    for round in strategy_guide:
        score_p1 += score_map_part_one.get(round, 0)
    return score_p1

# This is even uglier than part 1, I will really need to find a proper way to do this
def score_rounds_part_two(strategy_guide):
    score_map_part_two = {
        'A X': 3,
        'A Y': 4,
        'A Z': 8,
        'B X': 1,
        'B Y': 5,
        'B Z': 9,
        'C X': 2,
        'C Y': 6,
        'C Z': 7,
    }
    score_p2 = 0
    for round in strategy_guide:
        score_p2 += score_map_part_two.get(round, 0)
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

# Rock, paper, scissors /w strategy guide!
# chosing rock      =        1 point
# chosing paper     =        2 points
# chosing scissors  =        3 points
# loss              =        0 points
# draw              =        3 points
# win               =        6 points

# A, X, rock
# B, Y, paper
# C, Z, scissors

        # part 1     part 2
# A X -     4           3
# A Y -     8           4
# A Z -     3           8
# B X -     1           1
# B Y -     5           5
# B Z -     9           9
# C X -     7           2
# C Y -     2           6
# C Z -     6           7