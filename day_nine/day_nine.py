#%%
import numpy as np
import pandas as pd


def read_file(filename):
    # returns a list of instructions
    with open(filename) as f:
        a_list = f.read().split("\n")  # seperate each group by line
        a_list = list(map(int, a_list))
    return a_list


def find_invalid_no(input, preamble):
    """Find the first invalid number that doesn't use the first _ to sum"""
    preamble_list = input[0:preamble]  # list of possible numbers
    number_needed_list = []  # list of numbers needed
    counter = preamble
    invalid_no = 0
    while counter < len(input):
        # print("counter = " + str(counter))
        item = input[counter]
        # print(item)
        number_needed_list = [item - x for x in preamble_list]
        dup = item / 2  # can only have unique numbers
        if dup in number_needed_list:
            number_needed_list.remove(dup)
        # print(preamble_list)
        # print(number_needed_list)
        check = any(item in preamble_list for item in number_needed_list)
        if check is False:
            invalid_no = item
            # print("YIKES")
            return invalid_no
        preamble_list.append(item)  # add the most recent element to the list
        preamble_list.pop(0)  # take off the first element
        counter += 1

    return invalid_no


def find_invalid_no_2(input, preamble):
    """Get the invalid number then find the set of values that add to it in the list"""
    invalid_no = find_invalid_no(input, preamble)
    contagious_range = []
    min_pos = 0
    max_pos = 1
    while max_pos < len(input):
        contagious_range = input[min_pos:max_pos]
        sum_contagious_range = sum(contagious_range)
        if sum_contagious_range == invalid_no:
            break
        elif sum_contagious_range < invalid_no:
            max_pos += 1
        else:
            min_pos += 1

    sum_contagious_range = min(contagious_range) + max(contagious_range)
    return sum_contagious_range


#%%
test = "test.txt"
filename = "input.txt"
# input = read_file(test)
input = read_file(filename)
# Part 1
#%%
try:
    preamble = 25
    print(find_invalid_no(input, preamble))
except:
    print("Error")
#%%
# Part 2
try:
    preamble = 25
    print(find_invalid_no_2(input, preamble))
except:
    print("Error")

# %%
