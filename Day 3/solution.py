# Day 3

# Taking a string input, split it in half and match the character
# that exsists in both halfs. (only supposed to be one)
#
# Then turn that character into a score a-z is 1-26 and A-Z is 27-52
# 
# Finally, print the sum

import re
import json

def import_input_data():
    data = open("input.txt")
    data = data.read()
    input_data = data.split('\n')
    # Test input: answer is 157
    # input_data = [
    #     "vJrwpWtwJgWrhcsFMMfFFhFp",
    #     "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    #     "PmmdzqPrVvPwwTWBwg",
    #     "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    #     "ttgJtRGJQctTZtZT",
    #     "CrZsJsPPZsGzwwsLwLmpwMDw"
    # ]
    return input_data

def import_score_index():
    data = open("score_index.txt")
    data = data.read()
    # I though I would just be able to make i dict in a file and import it
    # and that the format would be recognized in python as a dict...
    # BUT it turns out that it adds "" to it like {"'a': 1, 'b': 2"}
    # It seems json came to the rescue!
    score_index = json.loads(data)
    return score_index

def split_data_and_match(input_data):
    matched_list = []
    for data in input_data: # split at half to match
        part_one, part_two = data[:len(data)//2], data[len(data)//2:]
        for character in part_one:
            match = re.search(character, part_two)
            if match:
                matched_list.append(character)
                break # break because only want one entry to list per string
    return matched_list

def generate_numbers_from_list(matched_list, score_index):
    score = 0
    for match in matched_list:
        score += score_index.get(match, 0)
    return score

def print_answer(pt1):
    print(pt1) # the answer is 7903

def main():
    input_data = import_input_data()
    score_index = import_score_index()
    matched_list = split_data_and_match(input_data)
    score_pt1 = generate_numbers_from_list(matched_list, score_index)
    print_answer(score_pt1)

if __name__ == "__main__":
    main()