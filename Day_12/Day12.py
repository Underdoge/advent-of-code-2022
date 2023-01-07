
def print_map(map):
    for line in map:
        print(line)

def print_steps(map,steps,end):
    end_y,end_x = end
    print("\nLen(steps):",len(steps))
    y = 0
    while y < len(map):
        x = 0
        while x < len(map[0]):
            if (y,x) in steps:
                if y == end_y and x == end_x:
                    print("E",end="")
                else:
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
                if y == end_y and x == end_x:
                    print("E",end="")
                else:
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
    y = 0
    while y < len(map):
        x = 0
        while x < len(map[0]):
            if map[y][x] == 'S':
                return y,x
            x += 1
        y += 1

def is_start(map,x,y):
    if map[y][x] == 'S':
        return True
    else:
        return False

def find_end(map):
    y = 0
    while y < len(map):
        x = 0
        while x < len(map[0]):
            if map[y][x] == 'E':
                return y,x
            x += 1
        y += 1

def fewest_steps(results):
    for route in results:
        if results.index(route) == 0:
            fewest = len(route)
        else:
            if len(route) < fewest:
                fewest = len(route)
    return fewest

def walk_map(start,end,steps,map,results):
    start_y,start_x = start
    if start != end:
        if (start_y,start_x + 1) not in steps and start_x + 1 <= len(map[0]) - 1 and (is_start(map,start_x,start_y) or ord(map[start_y][start_x]) + 1 >= ord(map[start_y][start_x + 1])):
            steps[start] = ">"
            walk_map((start_y,start_x + 1),end,steps.copy(),map,results)
        if (start_y,start_x - 1) not in steps and start_x - 1 >= 0 and (is_start(map,start_x,start_y) or ord(map[start_y][start_x]) + 1 >= ord(map[start_y][start_x - 1])):
            steps[start] = "<"
            walk_map((start_y,start_x - 1),end,steps.copy(),map,results)
        if (start_y + 1,start_x) not in steps and start_y + 1 <= len(map) - 1 and (is_start(map,start_x,start_y) or ord(map[start_y][start_x]) + 1 >= ord(map[start_y + 1][start_x])):
            steps[start] = "v"
            walk_map((start_y + 1,start_x),end,steps.copy(),map,results)
        if (start_y - 1,start_x) not in steps and start_y - 1 >= 0 and (is_start(map,start_x,start_y) or ord(map[start_y][start_x]) + 1 >= ord(map[start_y - 1][start_x])):
            steps[start] = "^"
            walk_map((start_y - 1,start_x),end,steps.copy(),map,results)
    else:
        steps[start] = "E"
        results.append(steps)
    return results
        
map = read_map("/Users/echapa/advent-of-code-2022/Day_12/test.txt")
print_map(map)
start = find_start(map)
end = find_end(map)
y,x = end
map[y][x] = 'z'
print("Fewest steps:",fewest_steps(walk_map(start,end,{},map,[])))


