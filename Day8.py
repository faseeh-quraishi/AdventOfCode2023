from _READFILE import FileToList

content = FileToList('Day8.txt')

def Task1(content):
    Instructions = [str(char) for char in content[0]]
    mapp = {}

    for node in content[2:]:
        node = node.split('=')
        mapp[node[0].strip()] = node[1].strip(' )(').split(',')
    
    Instruction = 0
    curr = 'AAA'
    steps = 0
    while curr != 'ZZZ':
        if Instructions[Instruction] == 'R':
            curr = mapp[curr][1].strip()    
        elif Instructions[Instruction] == 'L':
            curr = mapp[curr][0]
        
        steps += 1
        Instruction+=1
        
        Instruction %= len(Instructions)
    print(steps)

    file = open('Day8Sol1.txt','w')
    file = open('Day8Sol1.txt','a')
    file.write('Total Number of steps: ')
    file.write(str(steps))
    file.close()

    
# Task1(content)

def Task2(content):
    Instructions = [str(char) for char in content[0]]
    mapp = {}
    starting_nodes = []

    for node in content[2:]:
        node = node.split('=')
        childs = node[1].strip(' )(').split(',')
        mapp[node[0].strip()] = [childs[0],childs[1].strip()]

        if node[0].strip()[-1] == 'A':
            starting_nodes.append(node[0].strip())
    
    # end_loop = False
    # z_count = 0
    Instruction = 0
    # curr = 'AAA'
    steps = 0
    while True:
        z_count = 0
        for ind,node in enumerate(starting_nodes):
            if Instructions[Instruction] == 'R':
                starting_nodes[ind] = mapp[node][1]
                if starting_nodes[ind][-1] == 'Z':
                    z_count +=1
            else:
                starting_nodes[ind] = mapp[node][0]
                if starting_nodes[ind][-1] == 'Z':
                    z_count +=1
            # starting_nodes[ind] = mapp[node]
        
        steps += 1
        Instruction += 1
        Instruction %= len(Instructions)
        if z_count == len(starting_nodes):
            # end_loop = True
            break
        
        

        
        
        
        print(steps,starting_nodes)
    

    
    
    

Task2(content)