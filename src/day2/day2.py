import os
import re

dirname = os.path.dirname(__file__)
def part_1():
    with open(dirname + "/input.txt") as f:
        tally = 0
        for line in f.readlines():
            GAME = line.split(":")[0]
            GAME_ID = re.search("\d+$", GAME).group(0)
            GAMES = line.split(":")[1]
            GAMES = GAMES.split(";")
            cont = True
            for game in GAMES:
                m = {"blue": 14, "green": 13, "red": 12}
                BALLS = game.split(",")

                for ball in BALLS:
                    VAL = ball.strip().split(" ")[0]
                    COL = ball.strip().split(" ")[1]
                    m[COL] = m[COL] - int(VAL)
                for col in m:
                    if m[col] < 0:
                        cont = False
                        break
                if not cont:
                    break

            if cont:
                tally = tally + int(GAME_ID)
        print(tally)


def part_2():
    with open(dirname + "/input.txt") as f:
        suma = 0
        for line in f.readlines():
            GAME = line.split(":")[0]
            GAME_ID = re.search("\d+$", GAME).group(0)
            GAMES = line.split(":")[1]
            GAMES = GAMES.split(";")
            m = {"blue": 0, "green": 0, "red": 0}
            tally = 1
            for game in GAMES:

                BALLS = game.split(",")

                for ball in BALLS:
                    VAL = ball.strip().split(" ")[0]
                    COL = ball.strip().split(" ")[1]
                    m[COL] = max(m[COL], int(VAL))

            for i in m:
                tally = tally * m[i]
            suma = suma + tally
    print(suma)
                

PART = int(input("Part one or two? 1 or 2\n"))
if PART == 1:
    part_1()
else:
    part_2()