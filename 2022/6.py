def main():
    with open("6.txt") as f:
        lines = list(f)
    lines = [l.strip() for l in lines]
    lines = [l for l in lines if l]
    idxs = [get_start_index(l) for l in lines]
    print(idxs)


def get_start_index(line):
    stack = []
    for idx, c in enumerate(line):
        stack.append(c)
        if len(stack) > 14:
            stack.pop(0)
        if len(set(stack)) == 14:
            return idx + 1


if __name__ == "__main__":
    main()
