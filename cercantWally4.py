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