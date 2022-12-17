def main():
    with open("8.txt") as f:
        lines = list(f)
        lines = [l.strip() for l in lines if l.strip()]

    g = Grid(lines)

    total = 0
    for x in range(g.w):
        for y in range(g.h):
            total = max(total, g.get_score(x, y))
            # if g.is_visible(x, y):
            #     total += 1
    print(total)


class Grid:
    def __init__(self, data):
        self.w = len(data[0])
        self.h = len(data)
        self.data = data

    def get(self, x, y):
        return self.data[y][x]

    def dir_iter(self, x, y, dir):
        xs, ys = {"u": [0, -1], "d": [0, 1], "l": [-1, 0], "r": [1, 0]}[dir]
        x += xs
        y += ys
        while 0 <= x < self.w and 0 <= y < self.h:
            yield self.get(x, y)
            x += xs
            y += ys

    def is_visible(self, x, y):
        v = self.get(x, y)
        for d in "udlr":
            visible = True
            for tv in self.dir_iter(x, y, d):
                if tv >= v:
                    visible = False
                    break
            if visible:
                return True

    def get_score(self, x, y):
        v = self.get(x, y)
        total = 1
        for d in "udlr":
            score = 0
            for tv in self.dir_iter(x, y, d):
                score += 1
                if tv >= v:
                    break
            total *= score
        return total


if __name__ == "__main__":
    main()
