
def print_map(map):
    for line in map:
        print(line)

def print_steps(map,steps):
    print("\nLen(steps):",len(steps))
    y = 0
    while y < len(map):
        x = 0
        while x < len(map[0]):
            if (y,x) in steps:
                print(steps[(y,x)],end="")
            else:
                print(".",end="")
            x += 1
        print("")
        y += 1
    print("")
    y = 0
    while y < len(map):
        x = 0
        while x < len(map[0]):
            if (y,x) in steps:
                print(map[y][x],end="")
            else:
                print(".",end="")
            x += 1
        print("")
        y += 1

def read_map(file):
    map = []
    for line in open(file):
        line = line.rstrip()
        row = []
        for char in line:
            row.append(char)
        map.append(row)
    return map

def find_start(map):
    for line in map:
        for char in line:
            if char == 'S':
                return line.index(char),map.index(line)

def is_start(map,x,y):
    if map[y][x] == 'S':
        return True
    else:
        return False

def find_end(map):
    for line in map:
        for char in line:
            if char == 'E':
                return line.index(char),map.index(line),

def walk_map(start,steps,map):
    results = []
    start_y,start_x = start
    if map[start_y][start_x] != 'E':
        if (start_y,start_x + 1) not in steps and start_x + 1 <= len(map[0]) - 1 and (is_start(map,start_x,start_y) or ord(map[start_y][start_x]) + 1 >= ord(map[start_y][start_x + 1])):
            print("Right","start",start,"letter",map[start_y][start_x],"->",map[start_y][start_x + 1],"ord(map[start_y][start_x]) + 1 ",ord(map[start_y][start_x]) + 1,"ord(map[start_y][start_x + 1])",ord(map[start_y][start_x + 1]))
            steps[start] = ">"
            print("Steps:",steps)
            print_steps(map,steps)
            input()
            walk_map((start_y,start_x + 1),steps.copy(),map)
        if (start_y,start_x - 1) not in steps and start_x - 1 >= 0 and (is_start(map,start_x,start_y) or ord(map[start_y][start_x]) + 1 >= ord(map[start_y][start_x - 1])):
            print("Left","start",start,"letter",map[start_y][start_x],"->",map[start_y][start_x - 1],"ord(map[start_y][start_x]) + 1",ord(map[start_y][start_x]) + 1,"ord(map[start_y][start_x - 1])",ord(map[start_y][start_x - 1]))
            steps[start] = "<"
            print_steps(map,steps)
            input()
            walk_map((start_y,start_x - 1),steps.copy(),map)
        if (start_y + 1,start_x) not in steps and start_y + 1 <= len(map) - 1 and (is_start(map,start_x,start_y) or ord(map[start_y][start_x]) + 1 >= ord(map[start_y + 1][start_x])):
            print("Down","start",start,"letter",map[start_y][start_x],"->",map[start_y + 1][start_x],"ord(map[start_y][start_x]) + 1",(ord(map[start_y][start_x]) + 1),"ord(map[start_y + 1][start_x])",ord(map[start_y + 1][start_x]))
            steps[start] = "v"
            print_steps(map,steps)
            input()
            walk_map((start_y + 1,start_x),steps.copy(),map)
        if (start_y - 1,start_x) not in steps and start_y - 1 >= 0 and (is_start(map,start_x,start_y) or ord(map[start_y][start_x]) + 1 >= ord(map[start_y - 1][start_x])):
            print("Up","start",start,"letter",map[start_y][start_x],"->",map[start_y - 1][start_x],"ord(map[start_y][start_x]) + 1",ord(map[start_y][start_x]) + 1,"ord(map[start_y - 1][start_x])",ord(map[start_y - 1][start_x]))
            steps[start] = "^"
            print_steps(map,steps)
            input()
            walk_map((start_y - 1,start_x),steps.copy(),map)
    else:
        steps[start] = "E"
        print_steps(map,steps)
        print("Press any key to continue...")
        input()
        
print_map(read_map("/Users/echapa/advent-of-code-2022/Day_12/test.txt"))
print(find_start(read_map("/Users/echapa/advent-of-code-2022/Day_12/test.txt")))
print(find_end(read_map("/Users/echapa/advent-of-code-2022/Day_12/test.txt")))
start = find_start(read_map("/Users/echapa/advent-of-code-2022/Day_12/test.txt"))
walk_map(start,{},read_map("/Users/echapa/advent-of-code-2022/Day_12/test.txt"))

