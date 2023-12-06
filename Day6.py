from _READFILE import FileToList

path = 'Day6.txt'
content = FileToList(path)

def Task1(content):
    Time = content[0].split(':')[1].split()
    Distance = content[1].split(':')[1].split()
    TotalPossiblitiesPerRace = []

    for raceNo in range(len(Time)):
        PossiblitiesPerRace = []
        hold_time = 0 # This also refers to speed of the boat.
        
        
        while hold_time<=int(Time[raceNo]):
            remaining_time = int(Time[raceNo]) - hold_time
            projected_distance = hold_time * remaining_time
            if projected_distance > int(Distance[raceNo]):
                PossiblitiesPerRace.append((hold_time,projected_distance))
            hold_time +=1

        TotalPossiblitiesPerRace.append(len(PossiblitiesPerRace))

        product = 1
        for count in TotalPossiblitiesPerRace:
            product *= count
    
    file = open('Day6Sol1.txt','w')
    file = open('Day6Sol1.txt','a')
    for value in TotalPossiblitiesPerRace:
        file.write(str(value))
        file.write('\n')
    file.write('Total Sum: ')
    file.write(str(product))
    file.close()

Task1(content)

def Task2(content):
    Time = int(''.join(content[0].split(':')[1].split()))
    Distance = int(''.join(content[1].split(':')[1].split()))
    Possiblities = []
    hold_time = 0 # This also refers to speed of the boat.
    while hold_time <= Time:
        remaining_time = Time - hold_time
        projected_distance = hold_time * remaining_time
        if projected_distance > Distance:
            Possiblities.append((hold_time,projected_distance))
            break
        hold_time +=1

    hold_time = Time
    while hold_time > Possiblities[0][0]:
        remaining_time = Time - hold_time
        projected_distance = hold_time * remaining_time
        if projected_distance > Distance:
            Possiblities.append((hold_time,projected_distance))
            break
        hold_time -= 1

    numberOfWays = Possiblities[-1][0]-(Possiblities[0][0]-1)
    print(numberOfWays)
    file = open('Day6Sol2.txt','w')
    file = open('Day6Sol2.txt','a')
    for value in Possiblities:
        file.write(str(value))
        file.write('\n')
    file.write('Total Number of ways: ')
    file.write(str(numberOfWays))
    file.close()
        
Task2(content)