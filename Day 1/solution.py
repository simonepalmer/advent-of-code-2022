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

def import_data(): #import the data from the txt file
    data = open("input.txt")
    return data

def convert_data_to_list(data): #read data as a string and convert it to a list (on new line)
    data_str = data.read()
    data_list = data_str.split('\n')
    return data_list

def process_data_list(data_list): # process the list into sublists seperated by empty list indexes
    # processed_data_list = [list(sublist) for element, sublist in groupby(data_list, key = bool) if element]
    processed_data_list = []
    for element, sublist in groupby(data_list, key=bool):
        if element:
            processed_data_list.append(list(sublist))
    return processed_data_list

def get_sublist_sums(processed_data_list): # gets the sums of all sublists
    # sums_of_sublists = [sum(int(x) for x in sublist) for sublist in processed_data_list]
    sums_of_sublists = []
    for sublist in processed_data_list:
        sublist_sum = 0
        for x in sublist:
            sublist_sum += int(x)
        sums_of_sublists.append(sublist_sum)
    return sums_of_sublists

def print_highest_sublist_sum(list): # Sorts the list by sum and prints the highest sum
    list.sort()
    print("The sublist with the highest sum is:", list[-1],'\n')

def print_answer_for_part_two(list):
    list.sort()
    print("So the sum of the three highest are:", sum(list[-3:]), '\n')

def main():
    data = import_data()
    data_list = convert_data_to_list(data)
    processed_data_list = process_data_list(data_list)
    sums_of_sublists = get_sublist_sums(processed_data_list)
    print_highest_sublist_sum(sums_of_sublists)
    print_answer_for_part_two(sums_of_sublists)

    #Please explain why the thing described in the two following printed rows happens! :)
    print("from index -3 to but not including 0 '[-3:0]' seems to return: \"", sums_of_sublists[-3:0], "\" why is that?", sep='')
    print("But from index -3 to the end [-3:] returns the last three: \"",sums_of_sublists[-3:], "\" as expected", sep='')

if __name__ == "__main__":
    main()