import numpy as np
import pandas as pd


def read_file(filename):
    with open(filename) as f:
        expense_rpt = [int(line.rstrip()) for line in f]
    return expense_rpt


def find_product_two(expense_rpt):
    "find two items that sum to 2020 then multiply the items"
    item_needed = [2020 - x for x in expense_rpt]
    for item in expense_rpt:
        if item in item_needed:
            product = item * (2020 - item)

    return product


def find_product_three(expense_rpt):
    "find three items that sum to 2020 then multiply the items"
    item_needed = {
        2020 - x - y
        for x in expense_rpt
        for y in expense_rpt
        if x != y
        if 2020 - x - y > 0
    }
    items = []
    for item in expense_rpt:
        if item in item_needed:
            items.append(item)

    return np.prod(items)


expense_rpt_file = "day_one_input.txt"
expense_rpt = read_file(expense_rpt_file)
# Part 1
try:
    print(find_product_two(expense_rpt))
except:
    print("No two numbers sum to 2020.")

# Part 2
try:
    print(find_product_three(expense_rpt))
except:
    print("No three numbers sum to 2020.")
