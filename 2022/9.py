def main():
    with open("9_2.test") as f:
        lines = list(f)
        lines = [l.strip() for l in lines]
        lines = [l for l in lines if l]
    moves = [tuple(l.split(" ")) for l in lines]
    moves = [(d, int(n)) for d, n in moves]

    pts = [[0, 0] for _ in range(10)]

    reached = {(0, 0)}

    for d, n in moves:
        dx, dy = {
            "U": (0, -1),
            "D": (0, 1),
            "L": (-1, 0),
            "R": (1, 0),
        }[d]
        for _ in range(n):
            pts[0][0] += dx
            pts[0][1] += dy

            for idx in range(1, len(pts)):
                hx, hy = pts[idx - 1]
                tx, ty = pts[idx]
                pts[idx] = get_next_tail_loc(hx, hy, tx, ty)

            tx, ty = get_next_tail_loc(hx, hy, tx, ty)
            reached.add(tuple(pts[-1]))

    print(len(reached))


def get_next_tail_loc(hx, hy, tx, ty):
    dx = hx - tx
    dy = hy - ty
    if dx * dx + dy * dy < 4:
        return tx, ty
    if dx >= 1:
        tx += 1
    elif dx <= -1:
        tx -= 1
    if dy >= 1:
        ty += 1
    elif dy <= -1:
        ty -= 1
    return tx, ty


assert get_next_tail_loc(0, 0, 0, 0) == (0, 0)

if __name__ == "__main__":
    main()
