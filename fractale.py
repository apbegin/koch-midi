from math import trunc
__author__ = 'JJ'


import math




def _dist(p1, p2):
#Fonction _distX(x, y)
# qui calcul la distance horizontale entre deux points de
#   coordonees (x,y)
#RETOURNE un nombre
    dist_x_squared = (p2[0]-p1[0])**2 #dist entre x de p2 et p1
    dist_y_squared = (p2[1]-p1[1])**2 #dist entre y de p2 et p1

    return trunc(math.sqrt(dist_x_squared + dist_y_squared))

def _fraction_distance(p1, p2, fraction):
    #Fonction qui retourne les coordonnees d'un point se trouvant a une
    #certaine fraction de la distance entre deux points
    vect_points = [p2[0]-p1[0], p2[1]-p1[1]]   #Vecteur de distantce entre p1 et p2
    new_point = [p1[0] + fraction * vect_points[0],
                 p1[1] + fraction * vect_points[1]]   #Nouveau point = p1 + fraction distance p2-1
    return new_point


def trunct(n):
#fonction  h =trunct( 48/2n ) est utilisee pour calculer h de la recursion
# n est le niveau de recursion de la fonction musique
#RETOURNE un array de longueur 2
    hauteur = trunc(48/(2**n))
    
    return hauteur

def _genere_points(p1, p2, n):
    #fonction qui prend deux points et retourne 4 points selon de sorte
    #a faire un fractal de koch [p1--p3--p4--p5--p2} OU [A--C--D--E--B}
    p3 = _fraction_distance(p1, p2, 1/4)    #point C (ou p3) est sur la la droite AB
    p4 = _fraction_distance(p1, p2, 2/4)    #point D (ou p5) est sur la la droite AB
    p4[1] = trunct(n)                        #ajuste la hauteur de D selon trunct
    p5 = _fraction_distance(p1, p2, 3/4)    #point E (ou p5) est sur la la droite AB
    return [p1, p3, p4, p5, p2]

def musique(A, B, niveau, niveauMax):
    n = niveau
    init = 0
    next_points = _genere_points(A, B, n)
    if niveau == niveauMax:
        return [A[1], (_dist(A, B))] #on retourne la hauteur de A et la dist AB
    else:
        n += 1
        return [] + musique(next_points[0], next_points[1], n, niveauMax)+\
               musique(next_points[1], next_points[2], n, niveauMax) +\
               musique(next_points[2], next_points[3], n, niveauMax) +\
               musique(next_points[3], next_points[4], n, niveauMax)


a = [0, 0]
b = [8, 0]

print(_dist(a, b))
print(_fraction_distance(a, b, (1/4)))
print(_genere_points(a, b, 0))


d = musique(a, b, 0, 1)
print(d)

#Fonction MAIN
#On appel la fonction musique pour creer le tableau
#on cree un buffer
#On loop dans le tableau cree par musique pour pack les notes dans le buffer
#On read le file
        

"""
#Ecriture du hearder dans le fichier midi
def writeHeader():

    midiHeader ="4d54 6864 0000 0006 0001 0002 0080 4d54 "\
    "726b 0000 001a 0090 3c60 8100 3c00 003e "\
    "6081 003e 0000 4060 8100 4000 00ff 2f00 "\
    "4d54 726b 0000 0016 00c1 1800 9137 6082 "\
    "0037 0000 3960 8100 3900 00ff 2f00"
    print(midiHeader)
    midiHeader = bytes.fromhex(midiHeader)
    
    
    
    f = open('test.mid','wb')
    f.truncate()
    
    f.write(midiHeader)
    f.close()
"""