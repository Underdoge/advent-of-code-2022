
def print_map(map):
    for line in map:
        print(line)

def print_steps(map,steps):
    print("\nLen(steps):",len(steps))
    for line in map:
        for char in line:
            if (map.index(line),line.index(char)) in steps:
                print(steps[(map.index(line),line.index(char))],end="")
            else:
                print(".",end="")
        print("")
    print("")
    for line in map:
        for char in line:
            if (map.index(line),line.index(char)) in steps:
                print(char,end="")
            else:
                print(".",end="")
        print("")


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

def find_end(map):
    for line in map:
        for char in line:
            if char == 'E':
                return line.index(char),map.index(line),

def walk_map(start,steps,map):
    results = []
    start_y,start_x = start
    if map[start_y][start_x] != 'E':
        if (start_y,start_x + 1) not in steps and start_x + 1 <= len(map[0]) - 1 and map[start_y][start_x + 1] != 'S' and (map[start_y][start_x] == 'S' or ord(map[start_y][start_x]) >= ord(map[start_y][start_x + 1]) or ord(map[start_y][start_x]) + 1 == ord(map[start_y][start_x + 1])):
            #print("Right","start_y",start_y,"start_x",start_x,"letter",map[start_y][start_x],"comparing to",map[start_y][start_x + 1],"ord(map[start_y][start_x])",ord(map[start_y][start_x]),"ord(map[start_y][start_x + 1])",ord(map[start_y][start_x + 1]))
            steps[start] = ">"
            walk_map((start_y,start_x + 1),steps.copy(),map)
        if (start_y,start_x - 1) not in steps and start_x - 1 >= 0 and map[start_y][start_x - 1] != 'S' and (map[start_y][start_x] == 'S' or ord(map[start_y][start_x]) >= ord(map[start_y][start_x - 1]) or ord(map[start_y][start_x]) + 1 == ord(map[start_y][start_x - 1])):
            #print("Left","start_y",start_y,"start_x",start_x,"letter",map[start_y][start_x],"comparing to",map[start_y][start_x - 1],"ord(map[start_y][start_x])",ord(map[start_y][start_x]),"ord(map[start_y][start_x - 1])",ord(map[start_y][start_x - 1]))
            steps[start] = "<"
            walk_map((start_y,start_x - 1),steps.copy(),map)
        if (start_y + 1,start_x) not in steps and start_y + 1 <= len(map) - 1 and map[start_y + 1][start_x] != 'S' and (map[start_y][start_x] == 'S' or ord(map[start_y][start_x]) >= ord(map[start_y + 1][start_x]) or ord(map[start_y][start_x]) + 1 == ord(map[start_y + 1][start_x])):
            #print("Down","start_y",start_y,"start_x",start_x,"letter",map[start_y][start_x],"comparing to",map[start_y + 1][start_x],"ord(map[start_y][start_x])",ord(map[start_y][start_x]),"ord(map[start_y - 1][start_x])",ord(map[start_y - 1][start_x]))
            steps[start] = "v"
            walk_map((start_y + 1,start_x),steps.copy(),map)
        if (start_y - 1,start_x) not in steps and start_y - 1 >= 0 and map[start_y - 1][start_x] != 'S' and (map[start_y][start_x] == 'S' or ord(map[start_y][start_x]) >= ord(map[start_y - 1][start_x]) or ord(map[start_y][start_x]) + 1 == ord(map[start_y - 1][start_x])):
            #print("Up","start_y",start_y,"start_x",start_x,"letter",map[start_y][start_x],"comparing to",map[start_y - 1][start_x],"ord(map[start_y][start_x])",ord(map[start_y][start_x]),"ord(map[start_y - 1][start_x])",ord(map[start_y - 1][start_x]))
            steps[start] = "^"
            walk_map((start_y - 1,start_x),steps.copy(),map)
    else:
        steps[start] = "E"
        print_steps(map,steps)
        
print_map(read_map("/Users/echapa/advent-of-code-2022/Day_12/test.txt"))
print(find_start(read_map("/Users/echapa/advent-of-code-2022/Day_12/test.txt")))
print(find_end(read_map("/Users/echapa/advent-of-code-2022/Day_12/test.txt")))
start = find_start(read_map("/Users/echapa/advent-of-code-2022/Day_12/test.txt"))
walk_map(start,{},read_map("/Users/echapa/advent-of-code-2022/Day_12/test.txt"))

