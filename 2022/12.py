from dataclasses import dataclass
import re


def main():
    with open("12.txt") as f:
        lines = list(f)
    rows = [l.strip() for l in lines if l.strip()]
    rows = [[ord(val) for val in row] for row in rows]
    w = len(rows[0])
    h = len(rows)

    locs = set()
    for y, row in enumerate(rows):
        for x, val in enumerate(row):
            if chr(val) == "S":
                rows[y][x] = ord("a")
            elif chr(val) == "E":
                end = (x, y)
                rows[y][x] = ord("z")
            if chr(rows[y][x]) == "a":
                locs.add((x, y))
    print(locs)
    steps = 0
    while True:
        next_locs = set()
        for x, y in locs:
            val = rows[y][x]
            if x > 0:
                tv = rows[y][x - 1]
                if can_move(val, tv):
                    next_locs.add((x - 1, y))
            if x + 1 < w:
                tv = rows[y][x + 1]
                # print("adding", val, tv, can_move(val, tv))
                if can_move(val, tv):
                    next_locs.add((x + 1, y))
            if y > 0:
                tv = rows[y - 1][x]
                if can_move(val, tv):
                    next_locs.add((x, y - 1))
            if y + 1 < h:
                tv = rows[y + 1][x]
                if can_move(val, tv):
                    next_locs.add((x, y + 1))
        steps += 1
        if end in next_locs:
            break
        # print(next_locs)
        # input()
        locs = next_locs
    print(steps)


def can_move(val, tv):
    return tv <= val + 1


if __name__ == "__main__":
    main()
