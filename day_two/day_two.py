import numpy as np
import pandas as pd
import re


def read_file(filename):
    with open(filename) as f:
        a_list = [line.rstrip() for line in f]
    return a_list


def find_valid_pw_1(input):
    """Count valid passwords"""
    pw_count = 0
    for item in input:
        i = re.split("-| |: ", item)
        min = int(i[0])
        max = int(i[1])
        letter = i[2]
        pw = i[3]
        count = 0
        for c in pw:
            if c == letter:
                count += 1
        if min <= count <= max:
            pw_count += 1
    return pw_count


def find_valid_pw_2(input):
    """Count valid passwords"""
    pw_count = 0
    for item in input:
        i = re.split("-| |: ", item)
        pos_1 = int(i[0]) - 1  # -1 since index should start at 0
        pos_2 = int(i[1]) - 1
        letter = i[2]
        pw = i[3]
        is_pos_1 = pw[pos_1] == letter
        is_pos_2 = pw[pos_2] == letter
        if is_pos_1 != is_pos_2:
            pw_count += 1
    return pw_count


filename = "day_two_input.txt"
input = read_file(filename)
# Part 1
try:
    print(find_valid_pw_1(input))
except:
    print("Error")

# Part 2
try:
    print(find_valid_pw_2(input))
except:
    print("Error")
