from _READFILE import FileToList

path = 'Day4.txt'
content =  FileToList(path)

def Task1(content):
    ListOfScores = []
    for card in content:
        count = 0
        
        card = card.split(':')[1].split('|')
        winningNumbers = card[0].split()
        MyNumbers = card[1].split()
        for currNumber in MyNumbers:
            if currNumber in winningNumbers:
                count+=1
        if count == 0:
            continue
        ListOfScores.append(2**(count-1))
    
    

    file = open('Day4Sol1.txt','w')
    file = open('Day4Sol1.txt','a')
    for value in ListOfScores:
        file.write(str(value))
        file.write('\n')
    file.write('Total Sum: ')
    file.write(str(sum(ListOfScores)))
    file.close()


Task1(content)

def Task2(content):
    dictOfInstance = {}

    for i in range(1,len(content)+1):
        dictOfInstance[str(i)] = 1
         

    for CardId,card in enumerate(content):
        MatchingCount = 0
        
        card = card.split(':')[1].split('|')
        winningNumbers = card[0].split()
        MyNumbers = card[1].split()
        for currNumber in MyNumbers:
            if currNumber in winningNumbers:
                MatchingCount+=1
        for j in range(dictOfInstance[str(CardId+1)]):
            for i in range(MatchingCount):
                dictOfInstance[str(CardId+2+i)]+=1

    file = open('Day4Sol2.txt','w')
    file = open('Day4Sol2.txt','a')
    for value in dictOfInstance.values():
        file.write(str(value))
        file.write('\n')
    file.write('Total Sum: ')
    file.write(str(sum(dictOfInstance.values())))
    file.close() 





Task2(content)
