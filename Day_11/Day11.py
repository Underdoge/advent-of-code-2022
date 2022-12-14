import time
import functools

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
    return monkeys

def int_to_array(number):
    array = []
    for i in str(number)[::1]:
        array.append(int(i))
    return array

def array_to_int(array):
    return functools.reduce(lambda total, d: 10 * total + d, array, 0)

def array_add(array,x):
    if len(x) > len(array):
        y = array
        array = x
        x = y
    carry = 0
    i = len(array)
    j = len(x)
    k = 0
    while j > 0:
        sum = ((array[i-1] + x[j-1]) + carry)
        array[-1 -k] = sum % 10
        carry = int(sum / 10)
        j -= 1
        i -= 1
        k += 1
    while carry != 0:
        sum = array[i-1] + carry
        array[i-1] = sum % 10
        carry = int(sum / 10)
        i -= 1
    return array

def array_diff(array,x):
    if len(x) > len(array) or array_to_int(x) > array_to_int(array):
        y = array
        array = x
        x = y
    carry = 0
    i = len(x)
    j = len(array)
    k = 0
    while i > 0:
        if (array[j-1] >= x[i-1]):
            array[-1 -k] = (array[j-1] - x[i-1] - carry) % 10
            carry = 0
        elif (array[j-1] < x[i-1]):
            array[-1 -k] = (10+array[j-1] - x[i-1] - carry) % 10
            carry = 1
        i -= 1
        j -= 1
        k += 1
    print("array",array,"carry",carry)
    if carry == 1:
        array[-1 -k] = array[j-1] - carry
    return array

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
    original_array = array
    divisible = False
    if len(divisor) < 2:
        if divisor[0] == 2:
            if array[-1] % 2 == 0:
                divisible = True
        elif divisor[0] == 3:
            if array[-1] == 3 or array[-1] == 6 or array[-1] == 9:
                divisible = True
        elif divisor[0] == 5:
            if array[-1] == 0 or array[-1] == 5:
                divisible = True
        elif divisor[0] == 7:
            last = array[-1] * 2
            while len(array) > 1000:
                array = array_diff(array,int_to_array(last))
                last = array[-1] * 2
            if array_to_int(array) % 7 == 0:
                divisible = True
    else:
        if divisor == [1,1]:
            even = array[0::2]
            odd = array[1::2]
            even_sum = 0
            odd_sum = 0
            for num in even:
                even_sum += num
            for num in odd:
                odd_sum += num
            if even_sum == odd_sum:
                divisible = True
            else:
                if array_to_int(array_diff(int_to_array(even_sum),int_to_array(odd_sum))) % 11 == 0:
                    divisible = True
        elif divisor == [1,3]:
            last = array[-1] * 4
            while len(array) > 1000:
                array = array_add(array[:-1:],int_to_array(last))
            if array_to_int(array) % 13 == 0:
                divisible = True
        elif divisor == [1,7]:
            last = array[-1] * 9
            sum = array_add(array_mult_one_digit(array[:-1:],5),int_to_array(last))            
            if array_to_int(sum) % 17 == 0:
                divisible = True
        elif divisor == [1,9]:
            last = array[-1] * 2
            array = array_add(array[:-1:],int_to_array(last))
            while len(array) > 1000:
                last = array[-1] * 2
                array = array_add(array[:-1:],int_to_array(last))
            if array_to_int(array) % 19 == 0:
                divisible = True
        elif divisor == [2,3]:
            last = array[-1] * 7
            array = array_add(array[:-1:],int_to_array(last))
            if array_to_int(array) % 23 == 0:
                divisible = True
    #print(original_array,"divisable by",divisor,":",divisible)
    return divisible

def monkey_business(monkeys,rounds):
    for i in range(rounds):
        print("Round:",i)
        for monkey in monkeys:
            to_delete = []
            #print("monkey",monkeys.index(monkey),"items",monkey['items'],"operation",monkey['operation'],"test divisible by",monkey['test'],"true",monkey['true'],"false",monkey['false'])
            for item in monkey['items']:
                to_delete.append(item)
                if monkey['operation'][2] == 'old':
                    y = item
                    if monkey['operation'][1] == '*':
                        print(i,"doing item ^ 2")
                        new = array_mult(item,y)
                        print(i,"done doing item ^ 2")
                else:
                    if monkey['operation'][1] == '+':
                        y = int(monkey['operation'][2])
                        print(i,"doing item + y")
                        new = array_add(item,[y])
                        print(i,"done doing item + y")
                    else:
                        y = int_to_array(monkey['operation'][2])
                        if len(y) > 1:
                            print(i,"doing item * y (two digits)")
                            new = array_mult_two_digits(item,y)
                            print(i,"done doing item * y (two digits)")
                        else:
                            print(i,"doing item * y (one digit)")
                            new = array_mult_one_digit(item,y[0])
                            print(i,"done doing item * y (one digit)")
                if array_divisible_by(new,monkey['test']):
                    print(i,"inserting true")
                    monkeys[int(monkey['true'])]['items'].insert(0,new)
                else:
                    print(i,"inserting false")
                    monkeys[int(monkey['false'])]['items'].insert(0,new)
            for item in to_delete:
                monkey['inspected'] += 1
                print(i,"deleting")
                monkey['items'].remove(item)
                print(i,"done deleting")
    inspected = []
    for monkey in monkeys:
        print(f"Inspected {monkey['inspected']}")
        inspected.append(monkey['inspected'])
    inspected.sort(reverse=True)
    return inspected[0]*inspected[1]

tic = time.perf_counter()
#print(array_add([5,5,8,9,9,9],[3]))
monkey_business(read_monkeys_pt2('test.txt'),1000)
toc = time.perf_counter()
print(f"Took {toc - tic:0.4f} seconds")
