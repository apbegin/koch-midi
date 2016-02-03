from math import trunc
from _ast import List
__author__ = 'JJ'


import math



def _dist(p1, p2):
#Fonction _distX(x, y)
# qui calcul la distance horizontale entre deux points de
#   coordonees (x,y)
#RETOURNE un nombre
    dist_x_squared = (p2[0]-p1[0])**2 #dist entre x de p2 et p1
    dist_y_squared = (p2[1]-p1[1])**2 #dist entre y de p2 et p1

    return math.sqrt(dist_x_squared + dist_y_squared)

def _fraction_distance(p1, p2, fraction):
    #Fonction qui retourne les coordonnees d'un point se trouvant a une
    #certaine fraction de la distance entre deux points
    vect_points = [p2[0]-p1[0], p2[1]-p1[1]]   #Vecteur de distantce entre p1 et p2
    new_point = [p1[0] + fraction * vect_points[0],
                 p1[1] + fraction * vect_points[1]]   #Nouveau point = p1 + fraction distance p2-1
    return new_point




def _genere_points(p1, p2, n):
    #fonction qui prend deux points et retourne 4 points selon de sorte
    #a faire un fractal de koch [p1--p3--p4--p5--p2} OU [A--C--D--E--B}
    p3 = _fraction_distance(p1, p2, 1/4)    #point C (ou p3) est sur la la droite AB
    p4 = _fraction_distance(p1, p2, 2/4)    #point D (ou p5) est sur la la droite AB
    p4[1] = trunc(48/(2**n))                        #ajuste la hauteur de D selon trunct
    p5 = _fraction_distance(p1, p2, 3/4)    #point E (ou p5) est sur la la droite AB
    return [p1, p3, p4, p5, p2]

def musique(A, B, niveau, niveauMax):
    n = niveau
    
    next_points = _genere_points(A, B, n)
    if niveau == niveauMax:
        return [round(A[1]), (round(_dist(A, B)))] #on retourne la hauteur de A et la dist AB
    else:
        n += 1
        return [] + musique(next_points[0], next_points[1], n, niveauMax)+\
               musique(next_points[1], next_points[2], n, niveauMax) +\
               musique(next_points[2], next_points[3], n, niveauMax) +\
               musique(next_points[3], next_points[4], n, niveauMax)
               

#Ecriture du hearder dans le fichier midi


a = [0, 0]
b = [77760, 0]

print(_dist(a, b))
print(_fraction_distance(a, b, (1/4)))
print(_genere_points(a, b, 0))


koch_values = musique(a, b, 0, 5)

lst_note = []

channel = 90
volume = 60


lst_note.append([0,channel,0,volume])

dist_index = trunc(len(koch_values)/2)
for x in range(dist_index-1):
    lst_note.append([koch_values[2*x+1],channel,koch_values[2*x],volume])


print(koch_values)
print(lst_note)

#Section G du track header :
#nb de note x 4 pour le nombre de byte + 4 byte de la section F 
track_length = len(lst_note)*4 + 4

midiHeader ="4d 54 68 64 00 00 00 06 00 01 00 02 00 80 4d 54 72 6b " + str(track_length)
print(midiHeader)
midiHeader = bytes.fromhex(midiHeader)



f = open('test.mid','wb')
f.truncate()

f.write(midiHeader)
f.close()







    

#Fonction MAIN
#On appel la fonction musique pour creer le tableau
#on cree un buffer
#On loop dans le tableau cree par musique pour pack les notes dans le buffer
#On read le file
        


