from dataclasses import dataclass
import re


def main():
    with open("11.txt") as f:
        lines = list(f)
    lines = [l.strip() for l in lines]

    monkeys: list[Monkey] = []
    current = None
    for line in lines:
        match = re.match(r"Monkey (\d+):", line)
        if match:
            current = int(match.group(1))
            assert len(monkeys) == current
            monkeys.append(Monkey(current))
            continue
        if line.startswith("Starting items:"):
            monkeys[current].start_items = [
                int(e) for e in line[len("Starting items: ") :].split(",")
            ]
            continue
        if line.startswith("Operation: "):
            monkeys[current].operation = get_operation(line[len("Operation: ") :])
            continue
        if line.startswith("Test: divisible by "):
            monkeys[current].test_divisor = int(line[len("Test: divisible by ") :])
            continue
        if line.startswith("If true: throw to monkey "):
            monkeys[current].true_monkey = int(line[len("If true: throw to monkey ") :])
            continue
        if line.startswith("If false: throw to monkey "):
            monkeys[current].false_monkey = int(
                line[len("If false: throw to monkey ") :]
            )
            continue
        if line == "":
            continue
        assert False, line

    for idx in range(10000):
        run_round(monkeys)

    for m in monkeys:
        m.print()

    lst = [m.inspected for m in monkeys]
    lst.sort(reverse=True)
    print(lst[0] * lst[1])


@dataclass
class Monkey:
    idx: int
    inspected: int = 0
    start_items: list[int] = None
    test_divisor: int = None
    operation = None
    true_monkey: int = None
    false_monkey: int = None

    def print(self):
        print(
            f"Mokney {self.idx} inspected {self.inspected}: {', '.join(str(e) for e in self.start_items)}"
        )

    def run_operation(self, num: int):
        return self.operation(num)


def run_round(monkeys: list[Monkey]):
    N = 1
    for m in monkeys:
        N *= m.test_divisor
    for idx, monkey in enumerate(monkeys):
        while monkey.start_items:
            monkey.inspected += 1
            wl = monkey.start_items.pop(0)
            wl = monkey.run_operation(wl) % N
            # wl = wl // 3
            if wl % monkey.test_divisor == 0:
                monkeys[monkey.true_monkey].start_items.append(wl)
            else:
                monkeys[monkey.false_monkey].start_items.append(wl)


def get_operation(op: str):
    op = op.split(" ")
    assert len(op) == 5, op
    _, _, left, op, right = op
    if left == "old" and right == "old":
        if op == "+":
            return lambda old: old + old
        if op == "*":
            return lambda old: old * old
        raise Exception("unreachable")
    if left == "old" and right != "old":
        if op == "+":
            return lambda old: old + int(right)
        if op == "*":
            return lambda old: old * int(right)
        raise Exception("unreachable")
    raise Exception("unreachable", left, op, right)


if __name__ == "__main__":
    main()
