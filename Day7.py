from _READFILE import FileToList

path = 'Day7.txt'
content = FileToList(path)

def Task1(content):
    priorityMappings = {
                '5': 7,
                '41': 6,
                '32': 5,
                '311':4,
                '221':3,
                '2111':2,
                '11111':1
    }
    mappings = {
        'A':14,
        'K':13, 
        'Q':12, 
        'J':11, 
        'T':10, 
        '9':9, 
        '8':8, 
        '7':7, 
        '6':6, 
        '5':5, 
        '4':4, 
        '3':3,
        '2':2
    }
    
    TypeSegregatedList = [[] for i in range(len(priorityMappings.keys()))]
    
    for hand in content:
        hand = hand.split()

        tempCountDict = {}
        
        for card in hand[0]:
            if card in tempCountDict.keys():
                tempCountDict[card] += 1
            else:
                tempCountDict[card] = 1
        ListofCOunts = ''.join(sorted([str(i) for i in tempCountDict.values()],reverse = True))

        Priority= priorityMappings[ListofCOunts]
        tup = (tuple([mappings[card] for card in hand[0]]),hand[1])
        TypeSegregatedList[Priority-1].append(tup)
    
    for list in TypeSegregatedList:
        list.sort()

    i = 0
    sumOfProducts = 0
    rank = 1
    file = open('Day7Sol1.txt','w')
    file = open('Day7Sol1.txt','a')
    while i < len(TypeSegregatedList):
        for score in TypeSegregatedList[i]:
            sumOfProducts += int(score[-1])*rank
            rank+=1
        i+=1
    
    file.write('Total Sum: ')
    file.write(str(sumOfProducts))
    file.close()       
Task1(content)  


def Task2(content):
    priorityMappings = {
                '5': 7,
                '41': 6,
                '32': 5,
                '311':4,
                '221':3,
                '2111':2,
                '11111':1
    }
    mappings = {
        'A':14,
        'K':13, 
        'Q':12,  
        'T':10, 
        '9':9, 
        '8':8, 
        '7':7, 
        '6':6, 
        '5':5, 
        '4':4, 
        '3':3,
        '2':2,
        'J':1
        
    }
    
    TypeSegregatedList = [[] for i in range(len(priorityMappings.keys()))]
    
    for hand in content:
        hand = hand.split()
        tempCountDict = {}
        
        for card in hand[0]:

            if card in tempCountDict.keys():
                tempCountDict[card] += 1

            else:
                tempCountDict[card] = 1

        if 'J' in tempCountDict.keys() and tempCountDict['J'] < 5:
            temp = sorted([i for i in tempCountDict.values()],reverse = True)

            if tempCountDict['J'] == max(temp):
                temp[1]+=tempCountDict['J']
                temp.remove(tempCountDict['J'])

            else:
                temp[0]+=tempCountDict['J']
                temp.remove(tempCountDict['J'])  
            ListofCounts = ''.join([str(i) for i in temp])  

        else:
            ListofCounts = ''.join(sorted([str(i) for i in tempCountDict.values()],reverse = True))

        
            

        Priority= priorityMappings[ListofCounts]
        tup = (tuple([mappings[card] for card in hand[0]]),hand[1])
        TypeSegregatedList[Priority-1].append(tup)
    
    for list in TypeSegregatedList:
        list.sort()

    i = 0
    sumOfProducts = 0
    rank = 1
    file = open('Day7Sol2.txt','w')
    file = open('Day7Sol2.txt','a')
    while i < len(TypeSegregatedList):
        for score in TypeSegregatedList[i]:
            sumOfProducts += int(score[-1])*rank

            rank+=1
        i+=1
    print(sumOfProducts)
    file.write('Total Sum: ')
    file.write(str(sumOfProducts))
    file.close() 

# Task2(content)