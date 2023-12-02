from _READFILE import FileToList

path = 'Day2.txt'
# ---------------------------------------------------------------------
def Task1(path):
    games = FileToList(path)
    noOfTotalCubes = {
        'red': 12,
        'blue': 14,
        'green': 13
    }
    validGameIds = [] 
    sumOfGameIds = 0

    for game in games:
        currGameId = ''
        tempIndex = 5
        validGame = True

        while game[tempIndex] != ':':
            currGameId += game[tempIndex]
            tempIndex += 1
        
        game = game[tempIndex+2:].split(';')

        for round in game:
            round = round.split(',')

            for pick in round:
                numberOfCubesInCurrPick = int(pick.split()[0])

                if pick[-1] == 'e' and numberOfCubesInCurrPick <= noOfTotalCubes['blue']:
                    continue

                elif pick[-1] == 'n' and numberOfCubesInCurrPick <= noOfTotalCubes['green']:
                    continue

                elif pick[-1] == 'd' and numberOfCubesInCurrPick <= noOfTotalCubes['red']:
                    continue

                else:
                    validGame = False
                    break

            if not validGame:
                break

        if validGame:
           validGameIds.append(int(currGameId)) 
        
    sumOfGameIds = sum(validGameIds)
    print(noOfTotalCubes)
    file = open('Day2Sol1.txt','w')
    file = open('Day2Sol1.txt','a')
    for value in validGameIds:
        file.write(str(value))
        file.write('\n')
    file.write('Total Sum: ')
    file.write(str(sumOfGameIds))
    file.close()
            
    
Task1(path)
# -----------------------------------------------------------------------
def Task2(path):
    games = FileToList(path)
    productsOfMinCubesRequired = []
    
    for game in games:
        currGameId = ''
        tempIndex = 5
        minCubesRequiredforGame = {
            'red': 0,
            'blue': 0,
            'green': 0
        } 

        while game[tempIndex] != ':':
            currGameId += game[tempIndex]
            tempIndex += 1
        
        game = game[tempIndex+2:].split(';')

        for round in game:
            round = round.split(',')

            for pick in round:
                numberOfCubesInCurrPick = int(pick.split()[0])

                if pick[-1] == 'e' and numberOfCubesInCurrPick > minCubesRequiredforGame['blue']:
                    minCubesRequiredforGame['blue'] = numberOfCubesInCurrPick

                if pick[-1] == 'n' and numberOfCubesInCurrPick > minCubesRequiredforGame['green']:
                    minCubesRequiredforGame['green'] = numberOfCubesInCurrPick

                if pick[-1] == 'd' and numberOfCubesInCurrPick > minCubesRequiredforGame['red']:
                    minCubesRequiredforGame['red'] = numberOfCubesInCurrPick
        
        productOfCurrentGame = 1
        for noOfCubesRequired in minCubesRequiredforGame.values():
            productOfCurrentGame *= noOfCubesRequired
        productsOfMinCubesRequired.append(productOfCurrentGame)
    
    totalSumOfproducts = 0
    for product in productsOfMinCubesRequired:
        totalSumOfproducts += product

    file = open('Day2Sol2.txt','w')
    file = open('Day2Sol2.txt','a')
    for value in productsOfMinCubesRequired:
        file.write(str(value))
        file.write('\n')
    file.write('Total Sum: ')
    file.write(str(totalSumOfproducts))
    file.close()

Task2(path)
