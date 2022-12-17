from dataclasses import dataclass


def main():
    with open("7.txt") as f:
        lines = list(f)
        lines = [l.strip() for l in lines]
        lines = [l for l in lines if l]
    cmd = None
    outputs = []
    cmds = []
    for line in lines:
        if line.startswith("$ "):
            if cmd is not None:
                cmds.append((cmd, outputs))
                cmd = None
                outputs = []
            cmd = line[2:]
        else:
            outputs.append(line)
    if cmd is not None:
        cmds.append((cmd, outputs))

    root = Dir("root", {})
    stack = [root]
    for cmd, outputs in cmds:
        node = stack[-1]
        assert isinstance(node, Dir)
        if cmd == "ls":
            for elem in outputs:
                if elem.startswith("dir"):
                    name = elem[4:]
                    node.contents.setdefault(name, Dir(name, {}))
                else:
                    size, name = elem.split(" ")
                    size = int(size)
                    node.contents[name] = File(name, size)
        elif cmd.startswith("cd"):
            path = cmd.split(" ")[1]
            if path == "..":
                stack.pop()
            elif path == "/":
                stack = [stack[0]]
            else:
                node.contents.setdefault(path, Dir(path, {}))
                stack.append(node.contents[path])

    # print(list(root.get_small_dirs()))
    # print([elem.name for elem in root.get_small_dirs()])
    all_dirs = list(root.get_small_dirs())
    # print([e.name for e in all_dirs])
    sizes = [elem.get_size() for elem in all_dirs]
    sizes.sort()
    # print(sizes)
    # print(sum(sizes))
    overflow = root.get_size() - 40000000
    # print(overflow)
    for s in sizes:
        if s >= overflow:
            print(s)
            break


@dataclass
class File:
    name: str
    size: int

    def get_size(self):
        return self.size

    def traverse(self):
        pass

    def get_small_dirs(self):
        return []


@dataclass
class Dir:
    name: str
    contents: dict
    size: int = None

    def get_size(self):
        if self.size is not None:
            return self.size
        self.size = sum([elem.get_size() for elem in self.contents.values()])
        return self.size

    def get_small_dirs(self):
        yield self
        for elem in self.contents.values():
            for res in elem.get_small_dirs():
                yield res


if __name__ == "__main__":
    main()
