def main():
    with open("10.txt") as f:
        lines = list(f)
        lines = [l.strip() for l in lines if l.strip()]

    cmds = []
    for l in lines:
        l = l.split(" ")
        if l[0] == "noop":
            cmds.append(("noop",))
        elif l[0] == "addx":
            cmds.append(("noop",))
            cmds.append((l[0], int(l[1])))
        else:
            raise Exception(l[0])

    grid = [["." for _ in range(40)] for _ in range(6)]

    total = 0
    val = 1
    for idx, cmd in enumerate(cmds):
        col = idx % 40
        row = idx // 40
        if abs(val - col) <= 1:
            grid[row][col] = "#"
        cycle = idx + 1
        if (cycle + 40 - 20) % 40 == 0:
            print(val, cycle, val * cycle)
            total += val * cycle
        if cmd[0] == "addx":
            val += cmd[1]
    print(total)
    print("\n".join("".join(row) for row in grid))


if __name__ == "__main__":
    main()
