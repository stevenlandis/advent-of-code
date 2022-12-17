def main():
    with open("14.txt") as f:
        lines = list(f)
    lines = [l.strip() for l in lines]
    grid = {}
    for line in lines:
        points = [tuple(int(x) for x in pnt.split(",")) for pnt in line.split("->")]
        for i in range(len(points) - 1):
            x0, y0 = points[i]
            x1, y1 = points[i + 1]
            if x0 == x1:
                for y in range(min(y0, y1), max(y0, y1) + 1):
                    grid[(x0, y)] = "#"
            else:
                assert y0 == y1
                for x in range(min(x0, x1), max(x0, x1) + 1):
                    grid[(x, y0)] = "#"
    maxy = max([y for _, y in grid.keys()])

    n_sand = 0
    while True:
        x = 500
        y = 0
        if (x, y) in grid:
            break
        while True:
            if y == maxy + 1:
                grid[(x, y)] = "+"
                break
            elif (x, y + 1) not in grid:
                y += 1
            elif (x - 1, y + 1) not in grid:
                x -= 1
                y += 1
            elif (x + 1, y + 1) not in grid:
                x += 1
                y += 1
            else:
                grid[(x, y)] = "+"
                break
        n_sand += 1
    print(n_sand)


def print_grid(grid):
    pts = list(grid.keys())
    xs = [x for x, _ in pts]
    ys = [y for _, y in pts]
    x0 = min(xs)
    x1 = max(xs) + 1
    y0 = min(ys)


if __name__ == "__main__":
    main()
