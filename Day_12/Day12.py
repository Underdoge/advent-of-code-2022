
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
        start_x,start_y = start
        end_x,end_y = end
        if start_x + 1 < len(map[0]) and (char_to_num(map[start_y][start_x]) >= char_to_num(map[start_y][start_x + 1]) or char_to_num(map[start_y][start_x]) == char_to_num(map[start_y][start_x + 1] + 1) ) :
    else:
        return steps
        

    
print_map(read_map("test.txt"))

print(find_start(read_map("test.txt")))
print(find_end(read_map("test.txt")))

start = find_start(map)
end = find_end(map)
