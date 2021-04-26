#%%
import numpy as np
import pandas as pd
from typing import List
from collections import Counter


def read_file(filename):
    # returns an array of seats
    with open(filename) as f:
        a_list = [list(line)[:-1] for line in f.readlines()]
    return a_list


neighbors = [(-1, 0), (-1, -1), (-1, +1), (0, -1), (0, +1), (1, 1), (1, 0), (1, -1)]
Grid = List[List[str]]


def find_best_place(input):
    """Find the best place to sit"""
    occ_seats = 0
    l_list = []
    h_list = []
    rows = len(input)
    cols = len(input[0])
    change = True
    while change:
        l_list = []
        h_list = []
        for (x, y), value in np.ndenumerate(input):
            l_counter = 0
            # print(l_list)
            h_counter = 0
            # print(x, y, value)
            if value == "L":
                if x + 1 == rows:  # last row
                    if y + 1 == cols:  # last col
                        if input[x - 1][y - 1] == "#":
                            h_counter += 1
                        if input[x - 1][y] == "#":
                            h_counter += 1
                        if input[x][y - 1] == "#":
                            h_counter += 1
                    elif y == 0:  # first col
                        if input[x - 1][y + 1] == "#":
                            h_counter += 1
                        if input[x - 1][y] == "#":
                            h_counter += 1
                        if input[x][y + 1] == "#":
                            h_counter += 1
                    else:  # cols inbetween
                        if input[x - 1][y - 1] == "#":
                            h_counter += 1
                        if input[x - 1][y] == "#":
                            h_counter += 1
                        if input[x - 1][y + 1] == "#":
                            h_counter += 1
                        if input[x][y - 1] == "#":
                            h_counter += 1
                        if input[x][y + 1] == "#":
                            h_counter += 1
                elif x == 0:  # first row
                    if y + 1 == cols:  # last col
                        if input[x + 1][y - 1] == "#":
                            h_counter += 1
                        if input[x + 1][y] == "#":
                            h_counter += 1
                        if input[x][y - 1] == "#":
                            h_counter += 1
                    elif y == 0:  # first col
                        if input[x + 1][y + 1] == "#":
                            h_counter += 1
                        if input[x + 1][y] == "#":
                            h_counter += 1
                        if input[x][y + 1] == "#":
                            h_counter += 1
                    else:  # cols inbetween
                        if input[x + 1][y - 1] == "#":
                            h_counter += 1
                        if input[x + 1][y] == "#":
                            h_counter += 1
                        if input[x + 1][y + 1] == "#":
                            h_counter += 1
                        if input[x][y - 1] == "#":
                            h_counter += 1
                        if input[x][y + 1] == "#":
                            h_counter += 1
                else:  # rows inbetween
                    if y + 1 == cols:  # last col
                        if input[x + 1][y - 1] == "#":
                            h_counter += 1
                        if input[x + 1][y] == "#":
                            h_counter += 1
                        if input[x][y - 1] == "#":
                            h_counter += 1
                        if input[x - 1][y - 1] == "#":
                            h_counter += 1
                        if input[x - 1][y] == "#":
                            h_counter += 1
                    elif y == 0:  # first col
                        if input[x + 1][y + 1] == "#":
                            h_counter += 1
                        if input[x + 1][y] == "#":
                            h_counter += 1
                        if input[x][y + 1] == "#":
                            h_counter += 1
                        if input[x - 1][y + 1] == "#":
                            h_counter += 1
                        if input[x - 1][y] == "#":
                            h_counter += 1
                    else:  # cols inbetween
                        if input[x + 1][y - 1] == "#":
                            h_counter += 1
                        if input[x + 1][y] == "#":
                            h_counter += 1
                        if input[x + 1][y + 1] == "#":
                            h_counter += 1
                        if input[x][y - 1] == "#":
                            h_counter += 1
                        if input[x][y + 1] == "#":
                            h_counter += 1
                        if input[x - 1][y - 1] == "#":
                            h_counter += 1
                        if input[x - 1][y] == "#":
                            h_counter += 1
                        if input[x - 1][y + 1] == "#":
                            h_counter += 1
                if h_counter == 0:
                    l_list.append([x, y])
            elif value == "#":
                if x + 1 == rows:  # last row
                    if y + 1 == cols:  # last col
                        if input[x - 1][y - 1] == "#":
                            l_counter += 1
                        if input[x - 1][y] == "#":
                            l_counter += 1
                        if input[x][y - 1] == "#":
                            l_counter += 1
                    elif y == 0:  # first col
                        if input[x - 1][y + 1] == "#":
                            l_counter += 1
                        if input[x - 1][y] == "#":
                            l_counter += 1
                        if input[x][y + 1] == "#":
                            l_counter += 1
                    else:  # cols inbetween
                        if input[x - 1][y - 1] == "#":
                            l_counter += 1
                        if input[x - 1][y] == "#":
                            l_counter += 1
                        if input[x - 1][y + 1] == "#":
                            l_counter += 1
                        if input[x][y - 1] == "#":
                            l_counter += 1
                        if input[x][y + 1] == "#":
                            l_counter += 1
                elif x == 0:  # first row
                    if y + 1 == cols:  # last col
                        if input[x + 1][y - 1] == "#":
                            l_counter += 1
                        if input[x + 1][y] == "#":
                            l_counter += 1
                        if input[x][y - 1] == "#":
                            l_counter += 1
                    elif y == 0:  # first col
                        if input[x + 1][y + 1] == "#":
                            l_counter += 1
                        if input[x + 1][y] == "#":
                            l_counter += 1
                        if input[x][y + 1] == "#":
                            l_counter += 1
                    else:  # cols inbetween
                        if input[x + 1][y - 1] == "#":
                            l_counter += 1
                        if input[x + 1][y] == "#":
                            l_counter += 1
                        if input[x + 1][y + 1] == "#":
                            l_counter += 1
                        if input[x][y - 1] == "#":
                            l_counter += 1
                        if input[x][y + 1] == "#":
                            l_counter += 1
                else:  # rows inbetween
                    if y + 1 == cols:  # last col
                        if input[x + 1][y - 1] == "#":
                            l_counter += 1
                        if input[x + 1][y] == "#":
                            l_counter += 1
                        if input[x][y - 1] == "#":
                            l_counter += 1
                        if input[x - 1][y - 1] == "#":
                            l_counter += 1
                        if input[x - 1][y] == "#":
                            l_counter += 1
                    elif y == 0:  # first col
                        if input[x + 1][y + 1] == "#":
                            l_counter += 1
                        if input[x + 1][y] == "#":
                            l_counter += 1
                        if input[x][y + 1] == "#":
                            l_counter += 1
                        if input[x - 1][y + 1] == "#":
                            l_counter += 1
                        if input[x - 1][y] == "#":
                            l_counter += 1
                    else:  # cols inbetween
                        if input[x + 1][y - 1] == "#":
                            l_counter += 1
                        if input[x + 1][y] == "#":
                            l_counter += 1
                        if input[x + 1][y + 1] == "#":
                            l_counter += 1
                        if input[x][y - 1] == "#":
                            l_counter += 1
                        if input[x][y + 1] == "#":
                            l_counter += 1
                        if input[x - 1][y - 1] == "#":
                            l_counter += 1
                        if input[x - 1][y] == "#":
                            l_counter += 1
                        if input[x - 1][y + 1] == "#":
                            l_counter += 1
                if l_counter >= 4:
                    h_list.append([x, y])
            else:  # value == "."
                h_counter += 1  # do nothing

        for seat in l_list:
            input[seat[0]][seat[1]] = "#"

        for seat in h_list:
            input[seat[0]][seat[1]] = "L"

        if len(l_list) == 0 and len(h_list) == 0:
            change = False

    for (x, y), value in np.ndenumerate(input):
        if value == "#":
            occ_seats += 1

    return occ_seats


def first_seat(grid: Grid, i: int, j: int, di: int, dj: int) -> str:
    nr = len(grid)
    nc = len(grid[0])

    while True:
        i += di
        j += dj

        if 0 <= i < nr and 0 <= j < nc:
            c = grid[i][j]
            if c == "#" or c == "L":
                return c
        else:
            return "."


def next_value2(grid: Grid, i: int, j: int) -> str:
    counts = Counter(first_seat(grid, i, j, di, dj) for di, dj in neighbors)

    c = grid[i][j]

    if c == "L" and counts["#"] == 0:
        return "#"
    if c == "#" and counts["#"] >= 5:
        return "L"
    else:
        return c


def step2(grid: Grid) -> Grid:
    return [
        [next_value2(grid, i, j) for j, c in enumerate(row)]
        for i, row in enumerate(grid)
    ]


def find_best_place_2(grid: Grid) -> int:
    while True:
        next_grid = step2(grid)
        if next_grid == grid:
            break
        grid = next_grid

    return sum(c == "#" for row in grid for c in row)


#%%
test = "test.txt"
filename = "input.txt"
input = read_file(test)
input = read_file(filename)
# Part 1
#%%
try:
    print(find_best_place(input))
except:
    print("Error")
#%%
# Part 2
try:
    print(find_best_place_2(input))
except:
    print("Error")

# %%
