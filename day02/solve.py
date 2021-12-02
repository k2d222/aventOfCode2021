

file = open('input.txt')
pos = depth = aim = 0


with open('input.txt') as f:
    lines = f.readlines()

    # for ln in lines:
    #     dir, amount = ln.split()
    #     if dir == 'forward':
    #         pos += int(amount)
    #     elif dir == 'down':
    #         depth += int(amount)
    #     elif dir == 'up':
    #         depth -= int(amount)

    for ln in lines:
        dir, amount = ln.split()
        if dir == 'forward':
            pos += int(amount)
            depth += aim * int(amount)
        elif dir == 'down':
            aim += int(amount)
        elif dir == 'up':
            aim -= int(amount)

    print(pos * depth)
