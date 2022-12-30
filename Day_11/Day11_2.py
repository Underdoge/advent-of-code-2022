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
            str_items = line[16::].split(", ")
            int_items = []
            for item in str_items:
                int_items.append(int(item))
            monkey['items'] = int_items
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
    for i in range(rounds):
        print(i,end=" ")
        for monkey in monkeys:
            to_delete = []
            for item in monkey['items']:
                to_delete.append(item)
                if monkey['operation'][2] == 'old':
                    y = item
                else:
                    y = int(monkey['operation'][2])
                if monkey['operation'][1] == '+':
                    print(i,"doing item + y")
                    new = item + y
                    print(i,"done doing item + y")
                else:
                    if item == y:
                        new = item
                    else:
                        print(i,"doing item * y")
                        new = item * y
                        print(i,"done doing item * y")
                if new % monkey['test'] == 0:
                    print(i,"inserting true")
                    monkeys[int(monkey['true'])]['items'].insert(0,new)
                    print(i,"done inserting true")
                else:
                    print(i,"inserting false")
                    monkeys[int(monkey['false'])]['items'].insert(0,new)
                    print(i,"done inserting false")
            for item in to_delete:
                monkey['inspected'] += 1
                print(i,"deleting")
                monkey['items'].remove(item)
                print(i,"done deleting")
        #print_monkeys(monkeys)
    inspected = []
    for monkey in monkeys:
        print(f"\nInspected {monkey['inspected']}")
        inspected.append(monkey['inspected'])
    inspected.sort(reverse=True)
    return inspected[0]*inspected[1]

monkey_business(read_monkeys('test.txt'),20)