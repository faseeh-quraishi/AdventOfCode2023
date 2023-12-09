from _READFILE import FileToList

path = 'Day9.txt'
content = FileToList(path)

def Task1(content):
    extrapolated = []
    for series in content:
        MasterList = []
        series = [int(i) for i in series.split()]
        MasterList.append(series)
        
        
        while True:
            ZeroCount = 0
            tempList = []
            for i in range(1,len(MasterList[-1])):
                diff = MasterList[-1][i]-MasterList[-1][i-1]
                tempList.append(diff)
                if diff == 0:
                    ZeroCount +=1
            MasterList.append(tempList)
            
            if ZeroCount == len(MasterList[-1]):
                for i in range(len(MasterList)-2,-1,-1):
                    MasterList[i].append(MasterList[i][-1]+MasterList[i+1][-1])
                break
        extrapolated.append(MasterList[0][-1])
    print(sum(extrapolated))

    file = open('Day9Sol1.txt','w')
    file = open('Day9Sol1.txt','a')
    file.write('Total sum: ')
    file.write(str(sum(extrapolated)))
    file.close()
Task1(content)

def Task2(content):
    extrapolated = []
    for series in content:
        MasterList = []
        series = [int(i) for i in series.split()]
        MasterList.append(series)
        
        
        while True:
            ZeroCount = 0
            tempList = []
            for i in range(1,len(MasterList[-1])):
                diff = MasterList[-1][i]-MasterList[-1][i-1]
                tempList.append(diff)
                if diff == 0:
                    ZeroCount +=1
            MasterList.append(tempList)
            if ZeroCount == len(MasterList[-1]):
                for i in range(len(MasterList)-2,-1,-1):
                    MasterList[i].insert(0,MasterList[i][0]-MasterList[i+1][0])
                break
        extrapolated.append(MasterList[0][0])
    print(sum(extrapolated))
    file = open('Day9Sol2.txt','w')
    file = open('Day9Sol2.txt','a')
    file.write('Total sum: ')
    file.write(str(sum(extrapolated)))
    file.close()
Task2(content)