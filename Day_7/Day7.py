import sys

def build_tree (file,lineNum,tree):
    lines = 0
    for output in open(file).readlines()[lineNum:]:
        output = output.rstrip().split(" ")
        print(f"Line: {lineNum} lines: {lines} Command: {output} Tree: {tree}")
        lines += 1
        if output[0] == '$':
            if output[1] == 'cd':
                if output[2] != '..':
                    if output[2] not in tree:
                        print(f"Not in tree: Output 2: cd {output[2]} and tree {tree}")
                        tree[output[2]] = build_tree(file,lineNum+1,{})
                        return tree
                    else:
                        print(f"yes in tree")
                else:
                    return build_tree(file,lineNum+1,tree)
        else:
            if output[0] != 'dir' and output[0] != "": #is file
                tree[output[1]] = int(output[0])
        lineNum+=1
    return tree
    print("END")

print(build_tree(sys.argv[1],0,{}))

