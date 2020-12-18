import numpy as np
import pandas as pd
import re


def read_file(filename):
    with open(filename) as f:
        a_list = [line.rstrip() for line in f]
    return a_list


def find_tree_1(input):
    """Count how many trees were hit"""
    tree_count = 0
    col_count = 0
    for item in input:
        width = len(item)
        times_by = 1
        add_by = 0
        if width < col_count:  # make sure you have enough spaces
            spaces_needed = col_count - width
            times_by = (spaces_needed // width) + 1
            add_by = (spaces_needed % width) + 1
        item = item * times_by + item[0:add_by]
        if item[col_count] == "#":  # tree
            tree_count += 1
        col_count += 3
    # print("tree count: " + str(tree_count))

    return tree_count


def find_tree_2(input):
    """Count how many trees were hit with different slopes"""
    offset_list = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    mult_list = []
    height = len(input)
    for row_offset, col_offset in offset_list:
        slope = input.copy()
        tree_count = 0
        col_count = 0
        for row in range(0, height, row_offset):
            width = len(slope[row])
            times_by = 1
            add_by = 0
            if width <= col_count:  # make sure you have enough spaces
                spaces_needed = col_count - width
                times_by = (spaces_needed // width) + 1
                add_by = (spaces_needed % width) + 1
            slope[row] = slope[row] * times_by + slope[row][0:add_by]
            if slope[row][col_count] == "#":  # tree
                tree_count += 1
            col_count += col_offset
        mult_list.append(tree_count)

    result = np.prod(np.array(mult_list))

    return result


filename = "day_three_input.txt"
input = read_file(filename)
# Part 1
try:
    print(find_tree_1(input))
except:
    print("Error")

# Part 2
try:
    print(find_tree_2(input))
except:
    print("Error")
