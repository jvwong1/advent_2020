import numpy as np
import pandas as pd


def read_file(filename):
    passport_list = []
    with open(filename) as f:
        a_list = f.read().split("\n\n")  # seperate each passport by blank line
        a_list = [x.replace("\n", " ") for x in a_list]
        for line in a_list:
            if line.strip() != "":
                passport_dict = {}
                for item in line.split(" "):
                    key, value = item.split(":")
                    passport_dict[key] = value.rstrip()
                passport_list.append(passport_dict)

    return passport_list


class Passport:
    def __init__(
        self,
        byr=None,
        iyr=None,
        eyr=None,
        hgt=None,
        hcl=None,
        ecl=None,
        pid=None,
        cid=None,
    ):
        self.byr = byr
        self.iyr = iyr
        self.eyr = eyr
        self.hgt = hgt
        self.hcl = hcl
        self.ecl = ecl
        self.pid = pid
        self.cid = cid

    def is_valid(self):
        # cid is optional
        if (
            (self.byr is None)
            | (self.iyr is None)
            | (self.eyr is None)
            | (self.hgt is None)
            | (self.hcl is None)
            | (self.ecl is None)
            | (self.pid is None)
        ):
            return "invalid"
        return "valid"


def find_valid_passports_1(input):
    """Count how many passports are valid"""
    pp_count = 0
    for item in input:
        if (
            ("byr" not in item)
            | ("iyr" not in item)
            | ("eyr" not in item)
            | ("hgt" not in item)
            | ("hcl" not in item)
            | ("ecl" not in item)
            | ("pid" not in item)
        ):
            pass
        else:
            pp_count += 1

    print("pp count: " + str(pp_count))

    return pp_count


def find_valid_passports_2(input):
    """Count how many passports are valid"""
    pp_count = 0
    hcl_match = [
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
    for item in input:
        # print(item)
        # print((item["hgt"]))
        # print(len(item["pid"]))
        # print((item["pid"].isdigit()))
        if (
            ("byr" in item)
            & (("iyr" in item))
            & (("eyr" in item))
            & (("hgt" in item))
            & (("hcl" in item))
            & (("ecl" in item))
            & (("pid" in item))
        ):
            # print("here")
            if (
                ((int(item["byr"]) >= 1920) & (int(item["byr"]) <= 2002))
                & ((int(item["iyr"]) >= 2010) & (int(item["iyr"]) <= 2020))
                & ((int(item["eyr"]) >= 2020) & (int(item["eyr"]) <= 2030))
                & (
                    (
                        (
                            (item["hgt"][-2:] == "cm")
                            # & (int(item["hgt"][:-2]) >= 150)
                            # & (int(item["hgt"][:-2]) <= 193)
                        )
                        | (
                            (item["hgt"][-2:] == "in")
                            # & (int(item["hgt"][:-2]) >= 59)
                            # & (int(item["hgt"][:-2]) <= 76)
                        )
                    )
                )
                & (
                    (item["hcl"][:1] == "#")
                    & (len(item["hcl"]) == 7)
                    & (any(x in item["hcl"] for x in hcl_match) is False)
                )
                & (
                    (
                        any(
                            x in item["ecl"]
                            for x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
                        )
                    )
                )
                & ((item["pid"].isdigit()) & (len(item["pid"]) == 9))
            ):
                if item["hgt"][-2:] == "cm":
                    if (int(item["hgt"][:-2]) >= 150) & (int(item["hgt"][:-2]) <= 193):
                        pp_count += 1
                elif item["hgt"][-2:] == "in":
                    if (int(item["hgt"][:-2]) >= 59) & (int(item["hgt"][:-2]) <= 76):
                        pp_count += 1
                # print("valid")
            else:
                pass
                # print("invalid")
        else:
            pass
            # print("invalid")

    print("pp count: " + str(pp_count))

    return pp_count


test = "test.txt"
filename = "input.txt"
# input = read_file(test)
input = read_file(filename)
# Part 1
try:
    print(find_valid_passports_1(input))
except:
    print("Error")

# Part 2
try:
    print(find_valid_passports_2(input))
except:
    print("Error")
