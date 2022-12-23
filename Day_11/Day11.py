import pandas as pd

def print_monkeys(monkeys):
    for monkey in monkeys:
        print(f"Monkey {monkeys.index(monkey)}: {monkey}")
    print("")

def read_monkeys_pt2(file):
    monkeys = []
    i = 0
    for line in open(file).read().splitlines():
        line = line.strip()
        if i == 0:
            monkey = {}
        if i == 1:
            items = []
            for item in line[16::].split(", "):
                items.append(int_to_array(item))
            monkey['items'] = items
        if i == 2:
            monkey['operation'] = line[17::].split(" ")
        if i == 3:
            monkey['test'] = int_to_array(int(line.split(" ")[3]))
            print(f"Divisible by {int_to_array(int(line.split(' ')[3]))}")
        if i == 4:
            monkey['true'] = int(line.split(" ")[5])
        if i == 5:
            monkey['false'] = int(line.split(" ")[5])
            monkey['inspected'] = 0
            print(monkey)
            monkeys.append(monkey)
        i += 1
        if i == 7:
            i = 0
    #monks = pd.Series(monkeys)
    #print(monks.apply(lambda x: "Divisible by " + str(x['test'])))
    return monkeys

def int_to_array(number):
    array = []
    for i in str(number)[::1]:
        array.append(int(i))
    return array

def array_add(array,x):
    sum = []
    carry = 0
    i = len(array)
    sum.insert(0,(array[i-1] + x) % 10)
    carry = int((array[i-1] + x) / 10)
    i -= 1
    while i > 0:
        sum.insert(0,(array[i-1] + carry) % 10)
        carry = int((array[i-1] + carry) / 10)
        i -= 1
    if carry != 0:
        sum.insert(0,carry)
    return sum

def array_diff(array,x):
    print(array,x)
    diff = []
    carry = 0
    i = len(x)
    j = len(array)
    while i > 0:
        if (array[j-1] > x[i-1]):
            diff.insert(0,(array[j-1] - x[i-1] - carry) % 10)
            carry = 0
        elif (array[j-1] < x[i-1]):
            diff.insert(0,(10+array[j-1] - x[i-1] - carry) % 10)
            carry = 1
        i -= 1
        j -= 1
    if carry == 1:
        diff.insert(0,array[j-1] - carry)
    while len(array) - len(diff) > 0:
        diff.insert(0,array[j])
        j -= 1

    return diff

array = [1,2,3,4,5]
diff = [1,3]
print(array_diff(array,diff))

def array_mult_one_digit(array,x):
    mult = []
    carry = 0
    i = len(array)
    while i > 0:
        mult.insert(0,(array[i-1] * x + carry) % 10)
        carry = int((array[i-1] * x + carry) / 10)
        i -= 1
    if carry != 0:
        mult.insert(0,carry)
    return mult

def array_mult_two_digits(array,x):
    sum_1 = []
    sum_2 = []
    result = []
    carry = 0
    i = len(array)
    while i > 0:
        sum_1.insert(0,(array[i-1] * x[1] + carry) % 10)
        carry = int((array[i-1] * x[1] + carry) / 10)
        i -= 1
    if carry != 0:
        sum_1.insert(0,carry)
    i = len(array)
    sum_1.insert(0,0)
    sum_2.append(0)
    carry = 0
    while i > 0:
        sum_2.insert(0,(array[i-1] * x[0] + carry) % 10)
        carry = int((array[i-1] * x[0] + carry) / 10)
        i -= 1
    if carry != 0:
        sum_2.insert(0,carry)
    while len(sum_1) > len(sum_2):
        sum_2.insert(0,0)
    i = len(sum_2)
    carry = 0
    while i > 0:
        result.insert(0,(sum_1[i-1] + sum_2[i-1] + carry) % 10)
        carry = int((sum_1[i-1] + sum_2[i-1] + carry) / 10)
        i -= 1
    while result[0] == 0:
        result = result[1::]
    return result

def array_sum(arrays):
    sums = []
    carry = 0
    i = len(arrays[0])
    while i > 0:
        j = len(arrays)
        sum = arrays[j-1][i-1] + carry
        j -= 1
        while j > 0:
            sum += arrays[j-1][i-1]
            j -= 1
        carry = int(sum / 10)
        sum = sum % 10
        sums.insert(0,sum)
        i -= 1
    if carry != 0:
        sums.insert(0,carry)
    return sums

def array_mult(array_1,array_2):
    carry = 0
    mults = []
    i = len(array_2)
    while i > 0:
        mult = []
        j = len(array_1)
        carry = 0
        for x in range(len(mults)):
            mult.insert(0,0)
        while j > 0:
            mult.insert(0,(array_1[i-1] * array_2[j-1] + carry) % 10)
            carry = int((array_1[i-1] * array_2[j-1] + carry) / 10)
            j -= 1
        if carry != 0:
            mult.insert(0,carry)
        for x in range(len(array_1)+len(array_2)-len(mult)):
            mult.insert(0,0)
        mults.append(mult)
        i -= 1
    array_sums = array_sum(mults)
    while array_sums[0] == 0:
        array_sums = array_sums[1::]
    return array_sums

def array_divisible_by(array,divisor):
    divisable = False
    print("testing divisable",array,"by",divisor,end="")
    if len(divisor) < 2:
        if divisor[0] == "2":
            if array[-1] % 2 == 0:
                divisable = True
        elif divisor == "3":
            if array[-1] == 3 or array[-1] == 6 or array[-1] == 9:
                divisable = True
        elif divisor == "5":
            if array[-1] == 0 or array[-1] == 5:
                divisable = True

    print(":",divisable)
    return divisable

def monkey_business(monkeys,rounds):
    for i in range(rounds):
        for monkey in monkeys:
            to_delete = []
            print("monkey",monkeys.index(monkey),"items",monkey['items'],"operation",monkey['operation'],"test divisable by",monkey['test'],"true",monkey['true'],"false",monkey['false'])
            for item in monkey['items']:
                to_delete.append(item)
                if monkey['operation'][2] == 'old':
                    y = item
                    if monkey['operation'][1] == '*':
                        new = array_mult(item,y)
                        print("round",i,"monkey",monkeys.index(monkey),"array mult: ",item,"*",y,"=",new)
                else:
                    if monkey['operation'][1] == '+':
                        y = int(monkey['operation'][2])
                        new = array_add(item,y)
                    else:
                        y = int_to_array(monkey['operation'][2])
                        if len(y) > 1:
                            new = array_mult_two_digits(item,y)
                        else:
                            new = array_mult_one_digit(item,y[0])
                if array_divisible_by(new,monkey['test']):
                    print("inserting",new,"into monkey",monkey['true'])
                    monkeys[int(monkey['true'])]['items'].insert(0,new)
                else:
                    print("inserting",new,"into monkey",int(monkey['false']))
                    monkeys[int(monkey['false'])]['items'].insert(0,new)
            for item in to_delete:
                monkey['inspected'] += 1
                monkey['items'].remove(item)
        print_monkeys(monkeys)
    inspected = []
    for monkey in monkeys:
        print(f"Inspected {monkey['inspected']}")
        inspected.append(monkey['inspected'])
    inspected.sort(reverse=True)
    return inspected[0]*inspected[1]

#monkey_business(read_monkeys_pt2('input11.txt'),2)
