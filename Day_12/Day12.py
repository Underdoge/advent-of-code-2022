
def print_map(map):
    for line in map:
        print(line)

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

def walk_map(start,end,steps,map):
    steps.append(start)
    if start != end:
        print("Start:",start,"End:",end,"Steps:",steps,"len(map[0])",len(map[0]),"len(map)",len(map))
        start_x,start_y = start
        end_x,end_y = end
        if start_x + 1 < len(map[0]) and (ord(map[start_y][start_x]) >= ord(map[start_y][start_x + 1]) or ord(map[start_y][start_x]) == ord(map[start_y][start_x + 1]) + 1):
            print("Right")
            walk_map((start_y,start_x + 1),end,steps,map)
        if start_x - 1 > 0 and (ord(map[start_y][start_x]) >= ord(map[start_y][start_x - 1]) or ord(map[start_y][start_x]) == ord(map[start_y][start_x - 1]) + 1):
            print("Left")
            walk_map((start_y,start_x - 1),end,steps,map)
        if start_y + 1 < len(map) and (ord(map[start_y][start_x]) >= ord(map[start_y + 1][start_x]) or ord(map[start_y][start_x]) == ord(map[start_y + 1][start_x]) + 1):
            print("Down")
            walk_map((start_y,start_x - 1),end,steps,map)
        if start_y - 1 > 0 and (ord(map[start_y][start_x]) >= ord(map[start_y - 1][start_x ]) or ord(map[start_y][start_x]) == ord(map[start_y - 1][start_x]) + 1):
            print("Up")
            walk_map((start_y,start_x - 1),end,steps,map)
    else:
        return steps
        

    
print_map(read_map("test.txt"))

print(find_start(read_map("test.txt")))
print(find_end(read_map("test.txt")))

start = find_start(read_map("test.txt"))
end = find_end(read_map("test.txt"))

print("Steps:",walk_map(start,end,[],read_map("test.txt")))
