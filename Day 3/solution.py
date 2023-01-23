# Day 3

# part 1. Taking a string input, split it in half and match the character
# that exsists in both halfs. (only supposed to be one)
#
# Then turn that character into a score a-z is 1-26 and A-Z is 27-52
# 
# Finally, print the sum

# part 2. Every three lines are grouped, what is the common character
# in every set of 3?

import re
import json

def import_input_data():
    data = open("input.txt")
    data = data.read()
    input_data = data.split('\n')
    # Test input: answers are 157 and 70
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
    score_index = json.loads(data)
    return score_index

# part 1 solution
def split_data_and_match(input_data):
    matched_list = []
    # split at half length
    for data in input_data:
        part_one, part_two = data[:len(data)//2], data[len(data)//2:]
        # match character in part_one and part_two
        for character in part_one:
            match = re.search(character, part_two)
            if match:
                matched_list.append(character)
                break # break, only want 1 entry per index
    return matched_list

# part 2 solution
def split_to_sublists_and_match(input_data):
    lists_off_three = []
    for i in range(0, len(input_data), 3): # from 0 to length of input_data, increments of 3
        lists_off_three.append(input_data[i:i + 3]) # append current index + 3 (not including 3rd)
        
    common_list = [] 
    for sublist in lists_off_three:
        common = set(sublist[0]) # save the first string in set "common"
        for string in sublist[1:]: # for the following strings i.e [1:]
            common.intersection_update(string) # updates set with common characters in "string"
        if common: # if not empty (which it should not ever be)
            common_list.append(common.pop()) # append the (only) common char
    return common_list

def generate_numbers_from_list(list, score_index):
    score = 0
    for match in list:
        score += score_index.get(match, 0)
    return score

def main():
    input_data = import_input_data() # input
    score_index = import_score_index() # score table

    matched_list = split_data_and_match(input_data) # part 1 solution
    common_list = split_to_sublists_and_match(input_data) # part 2 solution

    #Generate the scores
    score_pt1 = generate_numbers_from_list(matched_list, score_index)
    score_pt2 = generate_numbers_from_list(common_list, score_index)

    print(score_pt1) # the answer is 7903
    print(score_pt2) # the answer is 2548

if __name__ == "__main__":
    main()