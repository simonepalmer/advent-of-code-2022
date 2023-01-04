# Fist stab at advent of code 2022
# Day 2

# This time around it wants the total amount of the top 3 highest sublists
# I also thought I would just run everything from main() this time.

from itertools import groupby

def main():
    data = open("input.txt")
    data_str = data.read()
    data_list = data_str.split('\n')

    processed_data_list = [list(sublist) for element, sublist in groupby(data_list, key = bool) if element]
    sums_of_sublists = [sum(int(x) for x in sublist) for sublist in processed_data_list]
    sums_of_sublists.sort()

    #Please explain why the thing described in the two following printed rows happens! :)
    print("from index -3 to but not including 0 '[-3:0]' seems to return: \"", sums_of_sublists[-3:0], "\" why is that?", sep='')
    print("But from index -3 to the end [-3:] returns the last three: \"",sums_of_sublists[-3:], "\" as expected", sep='')
    
    top_three = sum(sums_of_sublists[-3:])
    print("So the sum of the three highest are:", top_three)

if __name__ == "__main__":
    main()