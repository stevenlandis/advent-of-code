from dataclasses import dataclass
import re
from typing import Optional


def main():
    with open("16.test") as f:
        lines = [l.strip() for l in f if l.strip()]

    valves = [Valve(l) for l in lines]
    # for v in valves:
    #     print(v)
    solve(valves)


class Valve:
    def __init__(self, line: str):
        match = re.match(
            r"Valve (\w+) has flow rate=(-?\d+); tunnels? leads? to valves? (.*)", line
        )
        if match is None:
            print(line)
        self.name = match.group(1)
        self.rate = int(match.group(2))
        self.outs = [x for x in match.group(3).split(", ")]

    def __repr__(self):
        return f"Valve({self.name}, {self.rate}, {self.outs})"


@dataclass(frozen=True)
class Info:
    name_valve_map: dict[str, Valve]
    cost_map: dict[str, dict[str, int]]
    n_rates: int


class State:
    def __init__(self, time: int, pos: tuple[str, str], opened: list[str]):
        assert time >= 0
        assert len(pos) == 2
        self.time = time
        self.pos = pos
        self.opened = tuple(sorted(opened))

    def get_key(self):
        return (self.time, tuple(sorted(self.pos)), self.opened)

    def __eq__(self, other: "State"):
        return self.get_key() == other.get_key()

    def __hash__(self):
        return hash(self.get_key())

    def open(self, i: int):
        assert self.pos[i] not in self.opened
        return State(self.time, self.pos, [*self.opened, self.pos[i]])

    def move(self, pos: str, i: int):
        return State(self.time, (pos, self.pos[(i + 1) % 2]), self.opened)

    def tick(self):
        return State(self.time - 1, self.pos, self.opened)

    def __repr__(self):
        return f"State({self.time}, {self.pos}, {self.opened})"

    def get_choices_for_i(self, i: int, info: Info):
        choices: list[tuple[int, "State"]] = []
        if info.name_valve_map[self.pos[i]].rate > 0 and self.pos[i] not in self.opened:
            choices.append(
                (info.name_valve_map[self.pos[i]].rate * (self.time - 1), self.open(i))
            )
        for next in info.name_valve_map[self.pos[i]].outs:
            cost = info.cost_map[self.pos[i]][next]
            if cost > self.time:
                continue
            choices.append((0, self.move(next, i)))
        return choices

    def get_choices(self, info: Info) -> list[tuple[int, "State"]]:
        if self.time <= 1 or len(self.opened) == info.n_rates:
            return []
        choices = []
        for v0, s0 in self.get_choices_for_i(0, info):
            for v1, s1 in s0.get_choices_for_i(1, info):
                choices.append((v0 + v1, s1.tick()))
        return choices

    # def get_best_possible(self, info: Info):
    #     rates = [v.rate for v in info.name_valve_map.values() if v.rate > 0]
    #     rates.sort(reverse=True)
    #     score = 0
    #     for i in range(min(len(rates), self.time)):
    #         score += rates[i] * (self.time - i - 1)
    #     return score * 0.1


def get_all_reachable(name_valve_nap: dict[str, Valve], root: str):
    cache = {}

    def update_cache(node, val):
        if node == root:
            return
        if node not in cache:
            cache[node] = val
        else:
            cache[node] = min(cache[node], val)

    reached = set()

    def helper(node, depth):
        if node in reached:
            return
        reached.add(node)
        for out in name_valve_nap[node].outs:
            if name_valve_nap[out].rate > 0:
                update_cache(out, depth + 1)
            else:
                helper(out, depth + 1)
        reached.remove(node)

    helper(root, 0)

    return cache


def get_better_outs(name_valve_map: dict[str, Valve]):
    res = {}
    for name in name_valve_map:
        outs = get_all_reachable(name_valve_map, name)
        res[name] = outs
    return res


def solve(vs: list[Valve]):
    name_valve_map = {valve.name: valve for valve in vs}
    n_rates = len([1 for v in name_valve_map.values() if v.rate > 0])
    cost_map = get_better_outs(name_valve_map)
    better_name_valve_map = {
        v.name: Valve(
            f"Valve {v.name} has flow rate={v.rate}; tunnels lead to valves {', '.join(cost_map[v.name].keys())}"
        )
        for v in vs
    }
    for v in better_name_valve_map.values():
        print(v)

    info = Info(
        name_valve_map=better_name_valve_map,
        cost_map=cost_map,
        n_rates=n_rates,
    )

    cache: dict[State, int] = {}

    def helper(state: State):
        if state in cache:
            return cache[state]

        cache[state] = 0

        pairs = state.get_choices(info)
        pairs.sort(key=lambda pair: pair[0], reverse=True)

        bestScore = 0
        for score, choice in pairs:
            bestScore = max(bestScore, score + helper(choice))

        cache[state] = bestScore
        return cache[state]

    s0 = State(26, ("AA", "AA"), [])
    helper(s0)

    m = max(cache.values())
    print([s for s, v in cache.items() if v == m])
    print(m)

    s = s0
    while True > 0:
        bs = -1
        bst = None
        bval = None
        choices = s.get_choices(info)
        # print(s, [(score, choice, cache[choice]) for score, choice in choices])
        print(s)
        if not choices:
            break
        for val, choice in choices:
            ts = val + cache[choice]
            if ts > bs:
                bs = ts
                bst = choice
                bval = val
            s = bst
        # print(s, bval, bs)


if __name__ == "__main__":
    main()
