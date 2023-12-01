from _READFILE import FileToList
path = 'Day1.txt'
def Task1(path):
    content = FileToList(path)
    RecoveredValues = []
    digitsList = ['0','1','2','3','4','5','6','7','8','9']

    for line in content:
        currentLineNumber = ''
        for char in line:
            if char in digitsList:
                currentLineNumber+=char
                break
        for char in line[-1::-1]:
            if char in digitsList:
                currentLineNumber+=char
                break
        RecoveredValues.append(currentLineNumber)

    total = 0
    for value in RecoveredValues:
        total += int(value)

    file = open('Day1Sol1.txt','w')
    file = open('Day1Sol1.txt','a')
    for value in RecoveredValues:
        file.write(value)
        file.write('\n')
    file.write('Total Sum: ')
    file.write(str(total))
    file.close()

# --------------------------------------------------------------------------

def Task2(path):

    content = FileToList(path)
    RecoveredValues = []
    digitsList = ['0','1','2','3','4','5','6','7','8','9']
    digitsmapped = {
        'one':'1',
        'two':'2',
        'three':'3',
        'four':'4',
        'five':'5',
        'six':'6',
        'seven':'7',
        'eight':'8',
        'nine':'9'
    }
    spellings = digitsmapped.keys()
    max_spelling = max(len(spelling) for spelling in spellings)
    starting_chars = ['o','t','f','s','e','n']
    ending_chars = ['e','o','r','x','n','t']

    for line in content:
        currentLineNumber = ''

        for ind,char in enumerate(line):
            if char in digitsList:
                currentLineNumber += char
                break

            elif char in starting_chars:
                found = False
                window_size = max_spelling

                for i in range(window_size):
                    if line[ind:ind+(window_size-i)] in spellings:
                        currentLineNumber+=digitsmapped[line[ind:ind+(window_size-i)]]
                        found = True
                        break

                if found:
                    break
        
        for ind in range(len(line)-1,-1,-1):
            char = line[ind]
            if char in digitsList:
                currentLineNumber += char
                break

            elif char in ending_chars:
                found = False
                window_size = max_spelling

                for i in range(window_size):
                    window_word = line[(ind+1)-(window_size-i):ind+1]
                    if window_word in spellings:
                        currentLineNumber+=digitsmapped[window_word]
                        found = True
                        break

                if found:
                    break

        RecoveredValues.append(currentLineNumber)

    total = 0
    for value in RecoveredValues:
        total += int(value)

    file = open('Day1Sol2.txt','w')
    file = open('Day1Sol2.txt','a')
    for value in RecoveredValues:
        file.write(value)
        file.write('\n')
    file.write('Total Sum: ')
    file.write(str(total))
    file.close()
Task1(path)
Task2(path)







        
    