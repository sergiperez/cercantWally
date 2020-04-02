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