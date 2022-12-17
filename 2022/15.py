import re


def main():
    with open("15.txt") as f:
        lines = [l.strip() for l in list(f)]

    sensors = [Sensor(l) for l in lines]
    # size = 20
    size = 4000000
    for ty in range(size):
        if ty % 100000 == 0:
            print(ty)
        rs = [s.get_x_range(ty) for s in sensors]
        rs = [r for r in rs if r is not None]
        rs.sort(key=lambda r: r[0])
        assert rs[0][0] <= 0
        hx = rs[0][1]
        for i in range(1, len(rs)):
            tlx, thx = rs[i]
            if tlx > hx + 1:
                print(hx + 1, ty, (hx + 1) * 4000000 + ty)
                # return
            hx = max(hx, thx)
    # print(min_x, max_x)
    # count = 0
    # for x in range(min_x, max_x + 1):
    #     for s in sensors:
    #         if s.in_range(x, ty) and (x, ty) != (s.x, s.y) and (x, ty) != (s.bx, s.by):
    #             count += 1
    #             break
    # print(count)
    # n_beacons = len({s.bx for s in sensors if s.by == ty})
    # n_sensors = len({s.x for s in sensors if s.y == ty})
    # print(max_x - min_x + 1 - n_beacons - n_sensors)

    # grid = {}
    # for s in sensors:
    #     grid[(s.x, s.y)] = "S"
    #     grid[(s.bx, s.by)] = "B"
    # for idx, s in enumerate(sensors):
    #     print(f"{idx+1} / {len(sensors)}")
    #     r = 1
    #     done = False
    #     while not done:
    #         for coord in get_diamond_coords(s.x, s.y, r):
    #             if coord in grid:
    #                 if grid[coord] == "B":
    #                     done = True
    #             else:
    #                 grid[coord] = "#"
    #         r += 1

    # match = sorted([x for (x, y), val in grid.items() if y == ty and val == "#"])
    # # print(match)
    # print(len(match))


def get_diamond_coords(x: int, y: int, r: int):
    coords = set()
    for i in range(r):
        coords.add((x + i, y - r + i))
        coords.add((x + r - i, y + i))
        coords.add((x - i, y + r - i))
        coords.add((x - r + i, y - i))
    return coords


class Sensor:
    def __init__(self, line):
        match = re.match(
            r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)",
            line,
        )
        self.x = int(match.group(1))
        self.y = int(match.group(2))
        self.bx = int(match.group(3))
        self.by = int(match.group(4))
        dx = abs(self.x - self.bx)
        dy = abs(self.y - self.by)
        self.dist = dx + dy

    def get_x_range(self, y):
        dy = abs(self.y - y)
        if dy > self.dist:
            return None
        extra = self.dist - dy
        return (self.x - extra, self.x + extra)

    def in_range(self, x, y):
        return abs(self.x - x) + abs(self.y - y) <= self.dist

    def __repr__(self):
        return f"Sensor({self.x}, {self.y}, {self.bx}, {self.by})"


if __name__ == "__main__":
    main()
