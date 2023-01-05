# Advent of code 2022
# Day 2

# HOW DO I DO IT?

# Rock, paper, scissors /w strategy guide!
# chosing rock      =        1 point
# chosing paper     =        2 points
# chosing scissors  =        3 points
# loss              =        0 points
# draw              =        3 points
# win               =        6 points

# How many total points after doing all rounds according to the strategy guide?

# Test input series, A-C opponent choice, X-Z your choice:
# A Y
# B X
# C Z

# A, X, rock
# B, Y, paper
# C, Z, scissors

# READING THE INPUT
# This time I thought I would check if I can import the contents directly from the webpage
# instead of saving it to a file. I expect this to be possible?
# Then just turning it to a list on '\n' to get something like ['A Y', 'B X', 'C Z']

# SCORING RESULTS
# This is the tricky part. I mean, I could probably just do a massiv if/elif-statement
# in a for loop to run though the whole thing with pre-determined scores for each of the
# 9(?) outcomes. But that seems like very poor taste and should probably be avoided.

# I feel like a more elegant solution could be that a for loop reads though the series
# and scores 1, 2 or 3 based on X, Y and Z and 0, 3 or 6 extra points when comparing
# to A, B and C

# KEEPING TRACK OF SCORE
# I feel like a good way to keep track of the score is to just append each rounds score
# to a list and the sum it up in the end.


# Rough outline of what I have in mind:
def import_and_format_data():

    return strategy_guide

def score_each_round(strategy_guide):

    return score_list

def print_total_score(score_list):
    print(sum(scorelist))

def main():
    strategy_guide = import_and_format_data()
    score_list = score_each_round(strategy_guide)
    print_total_score(score_list)

if __name__ == "__main__":
    main()