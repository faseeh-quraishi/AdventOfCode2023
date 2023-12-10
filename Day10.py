from _READFILE import  FileToList

path = 'Day10.txt'
content = FileToList(path)

def Task1(content):
    groundList = []
    currLoction = (0,0)
    width = len(content[0])
    height = len(content)
    for row,line in enumerate(content):
        tempList = []
        for col,tile in enumerate(line):
            tempList.append(tile)
            if tile == 'S':
                currLoction = (row,col)
        groundList.append(tempList)
    
    # N = 0
    # E = 0
    # W = 0
    # S = 0
    # prevLocation = currLoction
    # curr_Tile = ''
    # while curr_Tile != 'S':
    #     if curr_Tile == '|' and (groundList[currLoction[0]][currLoction[1]] != '.' or groundList[currLoction[0]][currLoction[1]] != '-'):

    
    print(groundList,currLoction)


# Not complete and Task2 not started yet
Task1(content)
        
        