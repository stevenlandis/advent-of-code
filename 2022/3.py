def main():
    with open("3.txt") as fid:
        lines = list(fid)
    lines = [l.strip() for l in lines]
    lines = [l for l in lines if l]
    for l in lines:
        assert len(l) % 2 == 0
    vals = [get_common(l) for l in lines]
    print(sum(vals))


def main2():
    with open("3.txt") as fid:
        lines = list(fid)
    lines = [l.strip() for l in lines]
    lines = [l for l in lines if l]
    assert len(lines) % 3 == 0
    batches = [lines[i : i + 3] for i in range(0, len(lines), 3)]
    vals = [get_common2(b) for b in batches]
    print(sum(vals))


def get_common2(batch):
    common = set(batch[0]) & set(batch[1]) & set(batch[2])
    assert len(common) == 1
    return get_priority(next(iter(common)))


def get_common(line):
    n2 = len(line) // 2
    l = line[:n2]
    r = line[n2:]
    common = set(l) & set(r)
    assert len(common) == 1
    return get_priority(next(iter(common)))


def get_priority(c):
    if "a" <= c <= "z":
        return 1 + ord(c) - ord("a")
    return 27 + ord(c) - ord("A")


assert get_priority("a") == 1
assert get_priority("z") == 26
assert get_priority("A") == 27
assert get_priority("Z") == 52


if __name__ == "__main__":
    main2()
