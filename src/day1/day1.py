import os


# I/O handler
def solve():
    tally = 0
    dirname = os.path.dirname(__file__)
    with open(dirname + "/input.txt") as f:
        for line in f.readlines():
            if PART == 2:
                line = process(line)
                # Filter to keep numbers only
            r = [x for x in line if x.isnumeric()]
            # If only one number is detected, it is both the starting and last number
            if len(r) < 2:
                r.append(r[0])
            tally = int(r[0]) * 10 + int(r[-1]) + tally

    print(tally)


def process(s: str):
    # eightwo should evaluate as 82 so sprinkle in some harmless characters
    candidates = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e",
    }
    for key in candidates:
        s = s.replace(key, candidates[key])

    return s


PART = int(input("Part one or two? 1 or 2"))
if PART not in [1, 2]:
    print("ERROR!")
    raise ValueError


solve()
