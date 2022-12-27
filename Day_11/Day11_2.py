def print_monkeys(monkeys):
    for monkey in monkeys:
        print(f"Monkey {monkeys.index(monkey)}: {monkey}")
    print("")

def read_monkeys(file):
    monkeys = []
    i = 0
    for line in open(file).read().splitlines():
        line = line.strip()
        if i == 0:
            monkey = {}
        if i == 1:
            monkey['items'] = line[16::].split(", ")
        if i == 2:
            monkey['operation'] = line[17::].split(" ")
        if i == 3:
            monkey['test'] = int(line.split(" ")[3])
        if i == 4:
            monkey['true'] = int(line.split(" ")[5])
        if i == 5:
            monkey['false'] = int(line.split(" ")[5])
            monkey['inspected'] = 0
            monkeys.append(monkey)
        i += 1
        if i == 7:
            i = 0
    return monkeys

def monkey_business(monkeys,rounds):
    longest_item = 0
    for i in range(rounds):
        for monkey in monkeys:
            to_delete = []
            for item in monkey['items']:
                to_delete.append(item)
                if monkey['operation'][2] == 'old':
                    y = int(item)
                else:
                    y = int(monkey['operation'][2])
                if monkey['operation'][1] == '+':
                    new = int(item) + y
                else:
                    new = int(item) * y
                if new > longest_item:
                    longest_item = new
                if new % int(monkey['test']) == 0:
                    monkeys[int(monkey['true'])]['items'].insert(0,new)
                else:
                    monkeys[int(monkey['false'])]['items'].insert(0,new)
            for item in to_delete:
                monkey['inspected'] += 1
                monkey['items'].remove(item)
    inspected = []
    for monkey in monkeys:
        inspected.append(monkey['inspected'])
    inspected.sort(reverse=True)
    return inspected[0]*inspected[1]

monkey_business(read_monkeys('/Users/echapa/advent-of-code-2022/Day_11/input11.txt'),200)