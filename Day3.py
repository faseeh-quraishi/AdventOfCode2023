
    
from _READFILE import FileToList
path = 'Day3.txt'
content = FileToList(path)

def Task1(content):
    digits = ['0','1','2','3','4','5','6','7','8','9']
    Symbols = ('+ - * /  % & | ^ ~ < > = ! \' " # @ ( ) [ ] { } , : ` = ; $').split()
    maxLens = (len(content),len(content[0]))
    cordinatesOfSybmbols = []
    numbers = []

    # finding symbols co-ordinates
    for ind_row,line in enumerate(content):
        for ind_col,char in enumerate(line):
            if char in Symbols or char == '\\':
                cordinatesOfSybmbols.append((ind_row,ind_col))
    
    
    # findin numbers
    for x,y in cordinatesOfSybmbols:
        temp_number = ''
        
        if (content[x][y+1] in digits):
            temp_number+= content[x][y+1]
            i = 1
            while y+1+i<maxLens[1] and content[x][y+1+i] and content[x][y+1+i] in digits:
                temp_number+= content[x][y+1+i]
                i+=1
            numbers.append(int(temp_number))
            temp_number = ''
        
        if content[x+1][y+1] and (content[x+1][y+1] in digits) and (content[x+1][y] not in digits):
            temp_number += content[x+1][y+1]
            
            i = 1
            while y+1+i<maxLens[1] and content[x+1][y+1+i] and content[x+1][y+1+i] in digits:
                temp_number+= content[x+1][y+1+i]
                i+=1
            numbers.append(int(temp_number))
            temp_number = ''

        if content[x-1][y+1] and (content[x-1][y+1] in digits) and (content[x-1][y] not in digits):
            temp_number += content[x-1][y+1]
            i = 1
            while y+1+i<maxLens[1] and content[x-1][y+1+i] and content[x-1][y+1+i] in digits:
                temp_number+= content[x-1][y+1+i]
                i+=1
            numbers.append(int(temp_number))
            temp_number = ''

        if content[x][y-1] and (content[x][y-1] in digits):
            temp_number += content[x][y-1]
            i = 1
            while y-1-i>0 and content[x][y-1-i] and content[x][y-1-i] in digits:
                temp_number = content[x][y-1-i] + temp_number
                i+=1
            numbers.append(int(temp_number))
            temp_number = ''

        if content[x-1][y-1] and (content[x-1][y-1] in digits) and (content[x-1][y] not in digits):
            temp_number += content[x-1][y-1]
            i = 1
            while y-1-i>0 and content[x-1][y-1-i] and content[x-1][y-1-i] in digits:
                temp_number = content[x-1][y-1-i] + temp_number
                i+=1
            numbers.append(int(temp_number))
            temp_number = ''

        if content[x+1][y-1] and (content[x+1][y-1] in digits) and (content[x+1][y] not in digits):
            temp_number += content[x+1][y-1]
            i = 1
            while y-1-i>0 and content[x+1][y-1-i] and content[x+1][y-1-i] in digits:
                temp_number = content[x+1][y-1-i] + temp_number
                i+=1
            numbers.append(int(temp_number))
            temp_number = ''

        if content[x-1][y] and (content[x-1][y] in digits):
            temp_number += content[x-1][y]

            i = 1
            while y-i>0 and content[x-1][y-i] and content[x-1][y-i] in digits:
                temp_number = content[x-1][y-i] + temp_number
                i+=1
            i = 1
            while y+i<maxLens[1] and content[x-1][y+i] and content[x-1][y+i] in digits:
                temp_number+= content[x-1][y+i]
                i+=1
            numbers.append(int(temp_number))
            temp_number = ''

        if content[x+1][y] and (content[x+1][y] in digits):
            temp_number += content[x+1][y]
            i = 1
            while y-i>0 and content[x+1][y-i] and content[x+1][y-i] in digits:
                temp_number = content[x+1][y-i] + temp_number
                i+=1
            i = 1
            while y+i<maxLens[1] and content[x+1][y+i] and content[x+1][y+i] in digits:
                temp_number+= content[x+1][y+i]
                i+=1
            numbers.append(int(temp_number))
            temp_number = ''
        


    print(len(cordinatesOfSybmbols))
    print(len(numbers))

# Note: Not complete solution and Task2 is also missing
Task1(content)
