# Fist stab at advent of code 2022
# Day 1

# Unfortunately it probably took me around 5 hours to complete
# I have had little to no experience with manipulating data and it was very
# clear as every step of the way (except for printing the result, woho!)
# took massive amounts of googling to figure out how to achieve every step
# and then trying to understand why it actually did work so I don't just
# get into the habit och copy pasting stuff that works with no understanding
# of why it does... Still feels like I am a little bit though

from itertools import groupby

def import_data(): #Import the data and make it into a list seperated by '\n' (new line)
    data = open("input.txt")
    data_str = data.read()
    data_list = data_str.split('\n')
    return data_list

def process_data_list(data_list):
    # Creates a new list grouping sequential not empty indexes together seperated by the empty indexes (which are removed)
    processed_data_list = [list(sublist) for not_empty, sublist in groupby(data_list, key = bool) if not_empty]
    # Converting all sublists in processed_data_list from str to int and and make a new list with the sum of all sublists
    sums_of_sublists = [sum(int((x)) for x in sublist) for sublist in processed_data_list]
    return sums_of_sublists

def print_answer_for_part_one(list): # Sorts the list by sum and prints the highest sum
    list.sort()
    print("The sublist with the highest sum is:", list[-1],'\n')

def print_answer_for_part_two(list): # Prints the sum of the three highest sublists
    list.sort()
    print("So the sum of the three highest are:", sum(list[-3:]), '\n')

def main():
    data_list = import_data()
    sums_of_sublists = process_data_list(data_list)
    print_answer_for_part_one(sums_of_sublists)
    print_answer_for_part_two(sums_of_sublists)

    # Please explain why the thing described in the two following printed rows happens! :)
    print("from index -3 to but not including 0 '[-3:0]' seems to return an empty bracket \"[]\" like this: ", sums_of_sublists[-3:0], ", why is that?", sep='')
    print("But from index -3 to the end [-3:] returns the last three: \"",sums_of_sublists[-3:], "\" as expected", sep='')

if __name__ == "__main__":
    main()