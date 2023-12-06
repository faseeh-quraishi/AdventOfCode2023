from _READFILE import FileToList

path = 'Day5.txt'
content = FileToList(path)

def Task1(content):
    NeededSeeds = [int(i) for i in content[0].split(':')[1].split()]
    NeededLocations = []
    MasterDict ={
        'seed_soil':{},
        'soil_fertilizer':{},
        'fertilizer_water':{},
        'water_light':{},
        'light_temperature':{},
        'temperature_humidity':{},
        'humidity_location':{}
    }
    
    # for key in MasterDict.keys():
    #     for i in range(100):
    #         MasterDict[key][str(i)] = i
        

    keyNumber = -1
    for lineNo in range(len(content)):
        line = content[lineNo]
        NamesOfKeys = [i for i in (MasterDict.keys())]
        currKeyName = NamesOfKeys[keyNumber]
        line = line.split()
        if lineNo != 0:
            if line == []:
                continue
            
            elif line[1] == 'map:':
                keyNumber += 1
                continue
            
            else:
                source = int(line[1])
                destination = int(line[0])

                for i in range(int(line[2])):
                    MasterDict[currKeyName][str(source)] = destination
                    source+=1
                    destination+=1
    
    for seed in NeededSeeds:
        temp = seed
        try:
            for name in NamesOfKeys:
                tempDict = MasterDict[name]
                temp = tempDict[str(temp)]
        except:
            pass
        NeededLocations.append(temp)

    a = min(NeededLocations)
    print(a)

       

        
    
    # print(count)
# Task1 not complete and Task2 not attempted yet
Task1(content)