import string
import random

#creació de la llista de simbols
#https://docs.python.org/2/library/string.html
simbols=list(string.printable)

def initLandscape(landscape):
    rowsMax=random.randrange(10,20)
    colsMax=random.randrange(10,20)
    landscape = [["" for x in range(rowsMax)] for y in range(colsMax)] 
    return landscape

def populateLandscape(landscape):
    wally = False
    for row in range(len(landscape)):
        for column in range(len(landscape[0])):
          personatge = random.choice(simbols)
          landscape[row][column] = personatge
    
    #Posem a Wally
    rowInitialWally = random.randrange(5,len(landscape)-5)
    colInitialWally = random.randrange(5,len(landscape[0])-5)
    #direcció
    #0 -> hortizontal i a la dreta
    #1 -> horitzontal i a l'esquerra
    #2 -> vertical i cap avall
    #3 -> vertical i cap amunt
    direction = random.randrange(0,4)
    rowInc = 0
    colInc = 0
    if (direction == 0):
        rowInc = +1
    elif (direction == 1):
        rowInc = -1
    elif (direction == 2):
        colInc = +1
    elif (direction == 3):
        colInc = -1    
    
    landscape[rowInitialWally][colInitialWally] ="W"
    row = rowInitialWally
    col = colInitialWally
    for lletra in "ally":
        row = row + rowInc
        col = col + colInc
        landscape[row][col] = lletra
        
    return landscape
 
def whereIsWally(landscape,toFind):
    posicio = -1
    #Completeu el codi 
    return posicio

landscape=populateLandscape(initLandscape([[]]))

for i in range(len(landscape)):
    print(landscape[i])
print("Wally està en la posició "+str(whereIsWally(landscape,"Wally")))