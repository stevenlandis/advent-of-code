def main():
    stack_lines = []
    instr_lines = []
    with open("5.txt") as f:
        for line in f:
            line = line.strip("\n")
            if line == "":
                break
            stack_lines.append(line)
        for line in f:
            line = line.strip("\n")
            instr_lines.append(line)

    stacks = {}
    idx_to_key_map = {}
    idx = 0
    for part in stack_lines[-1].split(" "):
        if part != "":
            idx_to_key_map[idx] = part
            idx += 1
    stacks = {key: [] for key in idx_to_key_map.values()}
    for idx in range(len(stack_lines) - 2, -1, -1):
        line = stack_lines[idx]
        for col in range(1, len(line), 4):
            value = line[col]
            if value == " ":
                continue
            stacks[idx_to_key_map[(col - 1) // 4]].append(value)

    for line in instr_lines:
        parts = line.split(" ")
        N = int(parts[1])
        from_key = parts[3]
        to_key = parts[5]
        temp_stack = []
        for _ in range(N):
            temp_stack.append(stacks[from_key].pop())
        for _ in range(N):
            stacks[to_key].append(temp_stack.pop())

    print("".join(stack[-1] for stack in stacks.values()))


if __name__ == "__main__":
    main()
