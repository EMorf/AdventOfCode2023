import os

tally = 0 
dirname = os.path.dirname(__file__)
with open(dirname + "/input.txt") as f:

    for line in f.readlines():
        r = [x for x in line if x.isnumeric()]
        if len(r) < 2:
            r.append(r[0])
        tally = int(r[0]) * 10 + int(r[-1]) + tally

print(tally)


