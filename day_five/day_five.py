import numpy as np
import pandas as pd


def read_file(filename):
    with open(filename) as f:
        a_list = [line.rstrip() for line in f]
    return a_list


def calc_min_max(ch, min_no, max_no):
    if ch == "B":
        new_min = (max_no - min_no) / 2 + min_no
        new_max = max_no
    elif ch == "F":
        new_min = min_no
        new_max = (max_no - min_no) / 2 + new_min
    elif ch == "R":
        new_min = (max_no - min_no) / 2 + min_no
        new_max = max_no
    elif ch == "L":
        new_min = min_no
        new_max = (max_no - min_no) / 2 + new_min
    return int(new_min), int(new_max)


def find_max_seat_id_1(input):
    """Find each seat's ID then find the max"""
    seat_list = []
    for item in input:
        row_min = 0
        row_max = 127
        col_min = 0
        col_max = 7
        seat_id = 0
        # print(item)
        # print(row_min, row_max)
        for ch in item[0:7]:
            # print(ch)
            row_min, row_max = calc_min_max(ch, row_min, row_max)
            # print(row_min, row_max)
        for ch in item[7:10]:
            # print(ch)
            col_min, col_max = calc_min_max(ch, col_min, col_max)
            # print(col_min, col_max)

        seat_id = row_max * 8 + col_max
        seat_list.append(seat_id)

        # print(
        #     "row: "
        #     + str(row_max)
        #     + ", col: "
        #     + str(col_max)
        #     + ", seat_id: "
        #     + str(seat_id)
        # )

    max_seat_id = max(seat_list)
    return max_seat_id


def find_missing(lst):
    return [x for x in range(lst[0], lst[-1] + 1) if x not in lst]


def find_max_seat_id_2(input):
    """Find each seat's ID then find the missing seat_id"""
    seat_list = []
    for item in input:
        row_min = 0
        row_max = 127
        col_min = 0
        col_max = 7
        seat_id = 0
        for ch in item[0:7]:
            row_min, row_max = calc_min_max(ch, row_min, row_max)
        for ch in item[7:10]:
            col_min, col_max = calc_min_max(ch, col_min, col_max)

        seat_id = row_max * 8 + col_max
        seat_list.append(seat_id)

    missing_seat = find_missing(seat_list)
    return missing_seat


test = "test.txt"
filename = "input.txt"
# input = read_file(test)
input = read_file(filename)
# Part 1
try:
    print(find_max_seat_id_1(input))
except:
    print("Error")

# Part 2
try:
    print(find_max_seat_id_2(input))
except:
    print("Error")
