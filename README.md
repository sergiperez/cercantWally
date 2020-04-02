# Quarentena coding - setmana del 30 de març

## Cercant a Wally
![](https://pbs.twimg.com/media/ETo8MQjX0AIOWXJ.jpg)

En aquesta època de confinament només Wally es pot passejar. És fàcil cercar-lo. Tan fàcil com cercar una W en una llista de lletres.

Completeu el codi:
```python=
import string
import random

#creació de la llista de simbols
#https://docs.python.org/2/library/string.html
simbols=list(string.printable)

def initLandscape(landscape):
    for i in range(100):
        landscape.append("")
    return landscape

def populateLandscape(landscape):
    wally = False
    for posicio in range(100):
        personatge = random.choice(simbols)
        if (personatge == "W"):
            if ("W" not in landscape):
                wally = True
                landscape[posicio] = personatge
        else:    
            landscape[posicio] = personatge
    
    if (not wally):
        #Assegurem que hi hagi en Wally
        landscape[random.randrange(100)] ="W"    
    return landscape

def whereIsWally(landscape,toFind):
    posicio = -1
    #TODO
    #Completeu aquí el codi per fer la cerca de W (ally)
    return posicio

landscape=populateLandscape(initLandscape([]))
print(landscape)
print("Wally està en la posició "+str(whereIsWally(landscape,"W")))
```

## Cercant a Wally
![](https://i.ytimg.com/vi/o5XJJ4o64QI/maxresdefault.jpg)

Aquí ja és més difícil hi ha 4 persones, per simular aquesta complexitat ara haureu de cercar en Wally en una llista de lletres però heu de comprovar que aparegui consecutivament les lletres Wally.

Completeu el codi:
```python=
import string
import random

#creació de la llista de simbols
#https://docs.python.org/2/library/string.html
simbols=list(string.printable)

def initLandscape(landscape):
    for i in range(100):
        landscape.append("")
    return landscape

def populateLandscape(landscape):
    wally = False
    for posicio in range(100):
        personatge = random.choice(simbols)
        landscape[posicio] = personatge
    
    #Posem a Wally
    #Fins a 95 perquè hem de posar després quatre lletres més
    posicioInicialWally = random.randrange(95)
    landscape[posicioInicialWally] ="W"
    landscape[posicioInicialWally+1] ="a"
    landscape[posicioInicialWally+2] ="l"
    landscape[posicioInicialWally+3] ="l"
    landscape[posicioInicialWally+4] ="y"
    return landscape

def whereIsWally(landscape,toFind):
    posicio = -1
    #Completeu el codi
    return posicio

landscape=populateLandscape(initLandscape([]))
print(landscape)
print("Wally està en la posició "+str(whereIsWally(landscape,"Wally")))
```

## Cercant a Wally
![](https://lamenteesmaravillosa.com/wp-content/uploads/2015/05/wally-1024x768.jpg)

S'ha acabat el confinament i tots hem sortit a retrobar-nos com *locus*. Entremig de nosaltres hi ha en Wally, el trobarem? És com trobar el nom Wally en una matriu de lletres. El nom pot estar en vertical i amunt a avall o d'avall a amunt, horitzontal i d'esquerra a dreta o dreta a esquerra.

Completeu el codi:
```python=
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
```

## Cercant a Wally
![](https://www.xeduced.com/wp-content/uploads/2016/12/donde-esta-wally.jpg)

Heu vist que hi ha una millor manera de cercar el Wally, tan fàcil com si us el posen a primer pla.

Per això useu un diccionari i tan sols heu de dir en quina posició es troba cada persona.

Completeu el codi:
```python=
import string
import random

#creació de la llista de simbols
simbols=list(string.printable)

def populateLandscape(landscape):
    for i in range(random.randrange(50,100)):
        #Crear paraules de 5 lletres
        personatge=""
        for i in range(5):
            personatge = personatge + random.choice(simbols)
        landscape[personatge] = random.randrange(100)
    #Posem a Wally
    landscape["Wally"] = random.randrange(100)
    return landscape

def whereIsWally(landscape,toFind):
    posicio = -1
    #Codi que esn retorna a Wally
    return posicio

landscape=populateLandscape({})
print(landscape)
print("Wally està en la posició "+str(whereIsWally(landscape,"Wally")))
```

## Cercar qualsevol personatge

I si enlloc de fer una aplicació avorrida que només cerca en Wally, cerqui el personatge que digui l'usuari.

Com ho fem?
- l'usuari entra quin personatge vol cercar.
- restriccions al personatge que vol entrar:
    -  exercici 1 només ha de ser una lletra
    -  exercici 2 i 3 ha de tenir 5 lletres (Wally,Mario) 
    -  exercici 4 pot ser qualsevol paraula
- heu de modificar també les funcions que s'us passen fetes. **Heu d'usar paràmetres**


