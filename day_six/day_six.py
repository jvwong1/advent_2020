import numpy as np
import pandas as pd


def read_file_1(filename):
    # returns a list of sets because sets have unique values
    group_list = []
    with open(filename) as f:
        a_list = f.read().split("\n\n")  # seperate each group by blank line
        a_list = [x.replace("\n", " ") for x in a_list]
        for line in a_list:
            line = line.replace(" ", "")
            group_list.append(set(list(line)))

    return group_list


def read_file_2(filename):
    # returns a list of sets because sets have unique values and see all yes
    yes_list = []
    alphabet = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    with open(filename) as f:
        a_list = f.read().split("\n\n")  # seperate each group by blank line
        a_list = [x.replace("\n", " ") for x in a_list]
        for group in a_list:
            person_count = 0
            # print("new group: ", group)
            for person in group.split(" "):
                # print(person)
                person_count += 1
            # print(person_count)
            group = group.replace(" ", "")
            group_list = list(group)
            # print(group_list)
            if person_count == 1:
                yes_list.append(group_list)
            elif person_count > 1:
                group_list_over_1 = []
                for ch in alphabet:
                    if person_count == group_list.count(ch):
                        group_list_over_1.append(ch)
                yes_list.append(group_list_over_1)

        # print(yes_list)

    return yes_list


def find_yes(input):
    """Find how many yes answers each group has and sum the total"""
    yes_list = []
    for item in input:
        yes_count = len(item)
        yes_list.append(yes_count)
    yes_sum = sum(yes_list)

    return yes_sum


test = "test.txt"
filename = "input.txt"
# input = read_file(test)
# input = read_file(filename)
# Part 1
try:
    input = read_file_1(filename)
    print(find_yes(input))
except:
    print("Error")

# Part 2
try:
    input = read_file_2(filename)
    print(find_yes(input))
except:
    print("Error")


# def badd_read_file_2(filename):
#     # returns a list of sets because sets have unique values and see all yes
#     yes_list = []
#     with open(filename) as f:
#         a_list = f.read().split("\n\n")  # seperate each group by blank line
#         a_list = [x.replace("\n", " ") for x in a_list]
#         for group in a_list:
#             group_list=[]
#             person_count = 0
#             print("new group: ", group)
#             for person in group.split(" "):
#                 print("person: ", person)
#                 for answer in person:
#                     if person_count == 0:
#                         group_list.append(answer.replace(" ", ""))
#                     if person_count >= 1:
#                         if answer not in group_list:


#                 print("group_list:", group_list)
#                 person_count += 1
#                 print(person_count)

#             #group_list = group_list.replace(" ", "")
#             yes_list.append((list(group_list)))
#         print(yes_list)

#     return yes_list

# def bad_read_file_2(filename):
#     # returns a list of sets because sets have unique values and see all yes
#     yes_list = []
#     alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#     with open(filename) as f:
#         a_list = f.read().split("\n\n")  # seperate each group by blank line
#         a_list = [x.replace("\n", " ") for x in a_list]
#         for group in a_list:
#             group_list=[]
#             person_count = 0
#             print("new group: ", group)
#             for person in group.split(" "):
#                 print("person: ", person)
#                 person_list = []
#                 person_list[:] = person.replace(" ", "")
#                 group_list.append(person_list)
#                 print("group_list:", group_list)
#                 person_count += 1
#             print(person_count)
#             if person_count == 1:
#                 pass
#             elif person_count > 1:
#                 for ch in alphabet:

#             yes_list.append((list(group_list)))
#         print(yes_list)

#     return yes_list
