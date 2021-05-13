#%%
import numpy as np
import pandas as pd
from typing import Dict, List, NamedTuple


def read_file(filename):
    # returns sequence of actions
    with open(filename) as f:
        a_list = [line.rstrip() for line in f]
    return a_list


NESW = ["N", "E", "S", "W", "N", "E", "S", "W"]


def update_nesw_dict(nesw_dict: dict, action: str, value: int) -> dict:
    """get new location of ship and update dict"""
    if action == "N":
        nesw_dict["vert"] = nesw_dict["vert"] + value
    elif action == "E":
        nesw_dict["horiz"] = nesw_dict["horiz"] + value
    elif action == "S":
        nesw_dict["vert"] = nesw_dict["vert"] - value
    elif action == "W":
        nesw_dict["horiz"] = nesw_dict["horiz"] - value
    elif action == "L":
        ship_dir_idx = "".join(NESW).rindex(nesw_dict["direction"])
        if value == 90:
            ship_dir_idx -= 1
        elif value == 180:
            ship_dir_idx -= 2
        elif value == 270:
            ship_dir_idx -= 3
        nesw_dict["direction"] = NESW[ship_dir_idx]
    # print(NESW[ship_dir_idx])
    elif action == "R":
        ship_dir_idx = NESW.index(nesw_dict["direction"])
        if value == 90:
            ship_dir_idx += 1
        elif value == 180:
            ship_dir_idx += 2
        elif value == 270:
            ship_dir_idx += 3
        nesw_dict["direction"] = NESW[ship_dir_idx]
    #  print(NESW[ship_dir_idx])
    elif action == "F":
        ship_dir = nesw_dict["direction"]
        if ship_dir == "N":
            nesw_dict["vert"] = nesw_dict["vert"] + value
        elif ship_dir == "E":
            nesw_dict["horiz"] = nesw_dict["horiz"] + value
        elif ship_dir == "S":
            nesw_dict["vert"] = nesw_dict["vert"] - value
        elif ship_dir == "W":
            nesw_dict["horiz"] = nesw_dict["horiz"] - value
    return nesw_dict


def find_loc(input):
    """Find the Manhattan distance between that location and the ship's starting position"""
    # ship starts facing East
    nesw_dict = {"vert": 0, "horiz": 0, "direction": "E"}
    for item in input:
        action = item[0]
        val = int(item[1:])
        # print(action + ": " + str(val))
        nesw_dict = update_nesw_dict(nesw_dict=nesw_dict, action=action, value=val)
    # print(nesw_dict)
    man_dis = abs(nesw_dict["vert"]) + abs(nesw_dict["horiz"])
    return man_dis


class Action(NamedTuple):
    action: str
    amount: int

    @staticmethod
    def parse(raw: str):
        return Action(raw[0], int(raw[1:]))


class ShipAndWaypoint:
    ship_x: int = 0
    ship_y: int = 0
    ship_heading: int = 0

    waypoint_x: int = 10
    waypoint_y: int = 1

    def move(self, action: Action) -> None:
        if action.action == "N":
            self.waypoint_y += action.amount
        elif action.action == "S":
            self.waypoint_y -= action.amount
        elif action.action == "E":
            self.waypoint_x += action.amount
        elif action.action == "W":
            self.waypoint_x -= action.amount
        elif action.action == "L":
            # rotate the waypoint around the ship the given number of degrees
            for _ in range(action.amount // 90):
                self.waypoint_x, self.waypoint_y = -self.waypoint_y, self.waypoint_x
        elif action.action == "R":
            for _ in range(action.amount // 90):
                self.waypoint_x, self.waypoint_y = self.waypoint_y, -self.waypoint_x

        elif action.action == "F":
            self.ship_x += action.amount * self.waypoint_x
            self.ship_y += action.amount * self.waypoint_y
        else:
            raise ValueError(f"unknown action {action}")


def find_loc_2(input):
    """Find the Manhattan distance between that location and the ship's starting position"""
    # ship starts facing East
    saw = ShipAndWaypoint()
    for action in input:
        saw.move(action)

    man_dis = abs(saw.ship_x) + abs(saw.ship_y)
    return man_dis


#%%
test = "test.txt"
filename = "input.txt"
input = read_file(test)
# input = read_file(filename)
# Part 1
#%%
try:
    print(find_loc(input))
except:
    print("Error")
#%%
# Part 2
try:
    with open("input.txt") as f:
        raw = f.read()
        actions = [Action.parse(line) for line in raw.split("\n")]
    print(find_loc_2(actions))
except:
    print("Error")

# %%
