'''
Created on 26.11.2023

@author: Phoenix
'''
import random
import os
from zlib import Z_HUFFMAN_ONLY
import time

n = int(input("Gib eine Zahl ein: "))

if n <= 4:
    print("Ungueltig")
else:
    print("Gueltig")
    
p = int(input("Gib die Menge der Zahlenpare an diese muessen mehr als die Haelfte der Groesse des Feldes entsprechen:  "))

if p >= ((n/2)+1+int(n%2)):
    print("Gueltig")
else:
    print("Ungueltig")

#Erstellt eine Klasse mit allen Wichtigen Informationen 

class Feld():
    def __init__(self):
        self.x_koordinate = int
        self.y_koordinate = int
        self.belegt = None
        self.wert = int
        self.frei = None
        



def felderstellen_feld():
    zweid_array = []
    for i in range (n):
        zeile = []
        for j in range (n):
            feld = Feld()
            feld.x_koordinate = j
            feld.y_koordinate = i
            feld.wert = 0
            feld.belegt = False
            feld.frei = True
            zeile.append(feld)

        zweid_array.append(zeile)
    return zweid_array


zweideminsionale_liste = felderstellen_feld()

def arukone_schreiben():
    for zeile in zweideminsionale_liste:
        for feld in zeile: 
            print(feld.wert,end=" ")
        print()
    print()

def loesung_schreiben():
    for zeile in arukone_loesung:
        for i in zeile: 
            print(i,end=" ")
        print()
    print()



def randomX():
    x = random.randint(0,n-1)
    return int(x)
def randomY():
    y = random.randint(0,n-1)
    return int(y)


    

def zahlenfinder_x (zahl):
    for zeile in zweideminsionale_liste:
        for feld in zeile:
            if feld.wert == zahl:
                
                return feld.x_koordinate

def zahlenfinder_y (zahl):
    for zeile in zweideminsionale_liste:
        for feld in zeile:
            if feld.wert == zahl:
                
                return feld.y_koordinate
            
def zahlenfinder (zahl):
    for zeile in zweideminsionale_liste:
        for feld in zeile:
            if feld.wert == zahl:
                
                return feld
 

# setzt an zufällige stellen zahlen ein 
def zahleneinfuegen():
    i = 1
    while i <= (p):
        x = randomX()
        y = randomY()
        if zweideminsionale_liste[y][x].frei == True:
            zweideminsionale_liste[y][x].wert = i
            zweideminsionale_liste[y][x].frei = False
            i = i+1
    return zweideminsionale_liste



#findert die noch freihen möglichkeiten
def ereichbareFelder(zahl):
    xzahl=zahlenfinder_x(zahl)
    yzahl=zahlenfinder_y(zahl)
    freiefelder = []
    if yzahl + 1 < n: 
        if zweideminsionale_liste[yzahl+1][xzahl].frei == True:
               zweideminsionale_liste[yzahl+1][xzahl].frei = False
               freiefelder.append(zweideminsionale_liste[yzahl+1][xzahl])
    if yzahl - 1 >= 0:
        if zweideminsionale_liste[yzahl-1][xzahl].frei == True:
                   zweideminsionale_liste[yzahl-1][xzahl].frei = False
                   freiefelder.append(zweideminsionale_liste[yzahl-1][xzahl])
    if xzahl + 1 < n:         
        if zweideminsionale_liste[yzahl][xzahl+1].frei == True:
               zweideminsionale_liste[yzahl][xzahl+1].frei = False
               freiefelder.append(zweideminsionale_liste[yzahl][xzahl+1])
    if xzahl - 1 >= 0:   
        if zweideminsionale_liste[yzahl][xzahl-1].frei == True:
               zweideminsionale_liste[yzahl][xzahl-1].frei = False
               freiefelder.append(zweideminsionale_liste[yzahl][xzahl-1])
               
    
    for feld in freiefelder:  
        if feld.y_koordinate + 1 < n:    
            if zweideminsionale_liste[feld.y_koordinate +1][feld.x_koordinate].frei == True:
                zweideminsionale_liste[feld.y_koordinate +1][feld.x_koordinate].frei = False
                freiefelder.append(zweideminsionale_liste[feld.y_koordinate +1][feld.x_koordinate])

        if feld.y_koordinate - 1 >= 0:
            if zweideminsionale_liste[feld.y_koordinate-1][feld.x_koordinate].frei == True:
                zweideminsionale_liste[feld.y_koordinate-1][feld.x_koordinate].frei = False
                freiefelder.append(zweideminsionale_liste[feld.y_koordinate-1][feld.x_koordinate])

        if feld.x_koordinate + 1 < n:    
            if zweideminsionale_liste[feld.y_koordinate][feld.x_koordinate+1].frei == True:
                zweideminsionale_liste[feld.y_koordinate][feld.x_koordinate+1].frei = False
                freiefelder.append(zweideminsionale_liste[feld.y_koordinate][feld.x_koordinate+1])

        if feld.x_koordinate - 1 >= 0:
            if zweideminsionale_liste[feld.y_koordinate][feld.x_koordinate-1].frei == True:
                zweideminsionale_liste[feld.y_koordinate][feld.x_koordinate-1].frei = False
                freiefelder.append(zweideminsionale_liste[feld.y_koordinate][feld.x_koordinate-1])
        
    for feld in freiefelder:
        feld.frei = True
        
    return freiefelder


zahleneinfuegen()

levelWidth = n
levelHeight = n
 
level = zweideminsionale_liste
 
def naechsteBewegungBekommen(x, y):
    return {
        'left':  [x-1, y], 
        'right': [x+1, y],
        'up':  [x, y-1],
        'down':  [x, y+1]
    }.values()
 
def kuerzestenWegBekommen(level, startKoordinate, endKoordinate):
    wegFinden = [[startKoordinate]]
    besuchteKoordinaten = [startKoordinate]
    
    while wegFinden != []:
        aktuellerWeg = wegFinden.pop(0)
        aktuelleKoordinate = aktuellerWeg[-1]
        
        currentX, currentY = aktuelleKoordinate
        
        if aktuelleKoordinate == endKoordinate:
            return aktuellerWeg
        
        for nextKoordinate in naechsteBewegungBekommen(currentX, currentY):
            nextX, nextY = nextKoordinate
            
            if nextX < 0 or nextX >= levelWidth:
                continue
            
            if nextY < 0 or nextY >= levelHeight:
                continue
            
            if nextKoordinate in besuchteKoordinaten:
                continue
            
            if level[nextY][nextX].frei == False:
                continue
            
            wegFinden.append(aktuellerWeg + [nextKoordinate])
            besuchteKoordinaten += [nextKoordinate]

arukone_loesung = []

for zeile in zweideminsionale_liste:
    zeile_loesung = []
    for feld in zeile:
        zeile_loesung.append(feld.wert)
    arukone_loesung.append(zeile_loesung)
        

moeglicheZahlen = []
for x in range (1,p+1):
    moeglicheZahlen.append(x) 
while moeglicheZahlen != []:
    i = random.choice(moeglicheZahlen)
    moeglicheZahlen.remove(i)
    
    freieFelder = ereichbareFelder(i)
    startFeld = zahlenfinder(i)
    startFeld.frei = False
    zielFeld = freieFelder[random.randint(0,len(freieFelder)-1)]
    zweideminsionale_liste[zielFeld.y_koordinate][zielFeld.x_koordinate].wert = i
    zweideminsionale_liste[zielFeld.y_koordinate][zielFeld.x_koordinate].frei = True
    arukone_loesung[zielFeld.y_koordinate][zielFeld.x_koordinate] = i


    shortestPath = kuerzestenWegBekommen(level, [startFeld.x_koordinate,startFeld.y_koordinate], [zielFeld.x_koordinate,zielFeld.y_koordinate])
    
    zielFeld.frei = False
    
    for coordinate in shortestPath:
        x, y = coordinate
        level[y][x].wert = i
        level[y][x].frei = False

#Gibt die Lösung aus
print(n)
print (p)
loesung_schreiben()
arukone_schreiben()


# Funktion um Loesung in Datei zu schreiben fuer das Challenge-Programm (Datei wird immer ueberschrieben)
def speichere_datei():

    current_directory = os.path.dirname(__file__)


    output_file_path = os.path.join(current_directory, 'arukone0.txt')


    with open(output_file_path, 'w') as file:
        file.write(f"{n}\n")
        file.write(f"{p}\n")
        

        for row in arukone_loesung:
            file.write(' '.join(map(str, row)) + '\n')
        
        file.write("\n")
        


    print(f"Die Datei wurde unter '{output_file_path}' gespeichert.")

speichere_datei()


