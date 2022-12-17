def main():
    with open("8.txt") as f:
        lines = list(f)
        lines = [l.strip() for l in lines if l.strip()]
    g = Grid(lines)

    # print(g.get_score(2, 1))
    best = 0
    for x in range(g.w):
        for y in range(g.h):
            best = max(best, g.get_score(x, y))
    print(best)


# 209880
class Grid:
    def __init__(self, data):
        self.data = data
        self.w = len(data[0])
        self.h = len(data)

    def dir_iter(self, x, y, dir):
        xs, ys = {"u": [0, -1], "d": [0, 1], "l": [-1, 0], "r": [1, 0]}[dir]
        x += xs
        y += ys
        while 0 <= x < self.w and 0 <= y < self.h:
            yield self.get(x, y)
            x += xs
            y += ys

    def get(self, x, y):
        return self.data[y][x]

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


def get_score(g, x, y):
    h = len(g)
    w = len(g[0])
    v = g[y][x]

    # from top
    tscore = 0
    for i in range(y - 1, -1, -1):
        tscore += 1
        if g[i][x] >= v:
            break

    # from bottom
    bscore = 0
    for i in range(y + 1, h):
        bscore += 1
        if g[i][x] >= v:
            break

    # from left
    lscore = 0
    for i in range(x - 1, -1, -1):
        lscore += 1
        if g[y][i] >= v:
            break

    # from right
    rscore = 0
    for i in range(x + 1, w):
        rscore += 1
        if g[y][i] >= v:
            break
    # print(tscore, lscore, rscore, bscore)

    return tscore * bscore * lscore * rscore


def is_visible(g, x, y):
    h = len(g)
    w = len(g[0])
    v = g[y][x]

    # from top
    visible = True
    for i in range(0, y):
        if g[i][x] >= v:
            visible = False
            break
    if visible:
        return True

    # from bottom
    visible = True
    for i in range(y + 1, h):
        if g[i][x] >= v:
            visible = False
            break
    if visible:
        return True

    # from left
    visible = True
    for i in range(0, x):
        if g[y][i] >= v:
            visible = False
            break
    if visible:
        return True

    # from right
    visible = True
    for i in range(x + 1, w):
        if g[y][i] >= v:
            visible = False
            break
    if visible:
        return True

    return False


if __name__ == "__main__":
    main()
