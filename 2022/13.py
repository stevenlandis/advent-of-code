import json


def main():
    with open("13.txt") as f:
        lines = list(f)
    lines = [json.loads(l.strip()) for l in lines if l.strip()]
    pairs = [tuple(lines[idx : idx + 2]) for idx in range(0, len(lines), 2)]
    sum = 0
    for idx, (l, r) in enumerate(pairs):
        comp = get_order(l, r)
        if comp == -1:
            sum += idx + 1
    print(sum)

    signals = [Signal(l) for l in [*lines, [[2]], [[6]]]]
    signals.sort()
    # for s in signals:
    #     print(s)

    for idx, s in enumerate(signals):
        if s.val == [[2]]:
            start = idx + 1
        elif s.val == [[6]]:
            end = idx + 1
    print(start * end)


class Signal:
    def __init__(self, val):
        self.val = val

    def __lt__(self, other):
        return get_order(self.val, other.val) == -1

    def __repr__(self):
        return f"Signal: {str(self.val)}"


def get_order(l, r):
    if isinstance(l, int) and isinstance(r, int):
        if l < r:
            return -1
        if l == r:
            return 0
        return 1
    if isinstance(l, int) and isinstance(r, list):
        return get_order([l], r)
    if isinstance(l, list) and isinstance(r, int):
        return get_order(l, [r])
    if isinstance(l, list) and isinstance(r, list):
        for idx in range(max(len(l), len(r))):
            if idx >= len(l):
                return -1
            if idx >= len(r):
                return 1
            comp = get_order(l[idx], r[idx])
            if comp != 0:
                return comp
        return 0
    assert False, (l, r)


if __name__ == "__main__":
    main()
