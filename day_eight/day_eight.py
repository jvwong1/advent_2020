#%%
import numpy as np
import pandas as pd


def read_file(filename):
    # returns a list of instructions
    with open(filename) as f:
        a_list = f.read().split("\n")  # seperate each group by line
    return a_list


def find_acc(input):
    """Find how accumulater value before the loop starts again"""
    acc_count = 0
    used_instruction = []  # list of used of instruction position
    counter = 0
    while counter not in used_instruction:
        # print(counter)
        item = input[counter]
        # print(item)
        used_instruction.append(counter)
        if item[:3] == "acc":  # add to acc_count, next item
            if item[4] == "+":
                acc_count += int(item[5:])
            else:  # minus
                acc_count -= int(item[5:])
            counter += 1
        elif item[:3] == "jmp":  # jump to __
            if item[4] == "+":
                counter += int(item[5:])
            else:  # minus
                counter -= int(item[5:])
        elif item[:3] == "nop":  # next item
            counter += 1

    return acc_count


def get_acc_count(input):
    _counter = 0
    _max_counter = len(input)
    _acc_count = 0
    _used_instruction_pos = []  # list of used of instruction position
    while _counter not in _used_instruction_pos:
        # print(_counter)
        item = input[_counter]
        #  print(item)
        _used_instruction_pos.append(_counter)
        if item[:3] == "acc":  # add to acc_count, next item
            if item[4] == "+":
                _acc_count += int(item[5:])
            else:  # minus
                _acc_count -= int(item[5:])
            _counter += 1
        elif item[:3] == "jmp":  # jump to __
            if item[4] == "+":
                _counter += int(item[5:])
            else:  # minus
                _counter -= int(item[5:])
        elif item[:3] == "nop":  # next item
            _counter += 1
        if _counter == _max_counter:
            break
    # print("counter= " + str(_counter) + "acc_count= " + str(_acc_count))
    return _counter, _acc_count


def find_acc_2(input):
    """Find how accumulater value by changing one instruction
    so there is no infinite loop"""
    max_counter = len(input)
    counter = 0
    acc_count = 0
    used_instruction_pos = []  # list of used of instruction position
    used_instruction = []
    while counter not in used_instruction_pos:
        #  print(counter)
        item = input[counter]
        # print(item)
        used_instruction_pos.append(counter)
        used_instruction.append(item)
        if item[:3] == "acc":  # add to acc_count, next item
            if item[4] == "+":
                acc_count += int(item[5:])
            else:  # minus
                acc_count -= int(item[5:])
            counter += 1
        elif item[:3] == "jmp":  # jump to __
            if item[4] == "+":
                counter += int(item[5:])
            else:  # minus
                counter -= int(item[5:])
        elif item[:3] == "nop":  # next item
            counter += 1

    for pos in used_instruction_pos:
        changed_input = input.copy()
        if changed_input[pos][:3] == "acc":
            pass
        elif (changed_input[pos][:3] == "nop") and (changed_input[pos][4:] == "+0"):
            pass
        elif changed_input[pos][:3] == "jmp":
            # print("jmp= " + changed_input[pos])
            changed_input[pos] = "nop " + changed_input[pos][4:]
            # print("jmp= " + changed_input[pos])
            # print(changed_input)
            new_counter, new_acc_count = get_acc_count(changed_input)
            if new_counter == max_counter:
                # print("done")
                break
        elif changed_input[pos][:3] == "nop":
            # print("nop= " + changed_input[pos])
            changed_input[pos] = "jmp " + changed_input[pos][4:]
            # print("nop= " + changed_input[pos])
            new_counter, new_acc_count = get_acc_count(changed_input)
            if new_counter == max_counter:
                #   print("done")
                break
    return new_acc_count


#%%
test = "test.txt"
filename = "input.txt"
# input = read_file(test)
input = read_file(filename)
# Part 1
#%%
try:
    print(find_acc(input))
except:
    print("Error")
#%%
# Part 2
try:
    print(find_acc_2(input))
except:
    print("Error")