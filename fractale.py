from math import trunc
__author__ = 'JJ'


#Fonction MAIN
#On appel la fonction musique pour cr�er le tableau
#on cr�e un buffer
#On loop dans le tableau cr�� par musique pour pack les notes dans le buffer
#On read le file

if __name__ == '__main__':
    
    A = 0x24
    B = 0x54
    h = getH(0)




#Fonction _distX(x, y)
# qui calcul la distance horizontale entre deux points de
#   coordon�es (x,y)
#RETOURNE un nombre

    
        
        


#fonction  h =trunc( 48/2n ) est utilis�e pour calculer h de la r�cursion
# n est le niveau de r�cursion de la fonction musique
#RETOURNE un entier

def getH(n):
    
    h = trunc(48/2**n)
    
    return h

#Fonction musique()
#qui agit comme suit. Si niveauMax == niveau, alors la fonction �met une note dont la
#dur�e est la distance entre A et B sur l�axe horizontal. La hauteur de ce son est celle du
#point A. La dur�e de cette note correspond � la longueur du segment (A,B) sur l�axe
#horizontal. Si niveau < niveauMax, alors la fonction trouve la position des points C, D
#et E et s�invoque r�cursivent sur les segments (A,D), (D,C), (C,E) et (E,B).
    #ACCORDING to le schema et la d�finition d'une forme de koch, le point C
    #est toujours au MILIEU du segment
    #RETOURNE un tableau de notes (note + longueur)
    #A et B commencent a une hauteur de 48, soit Middle-C ou x3C en hexa
    
def musique(A,B,niveau,niveauMax):
    if niveauMax == niveau:
        time = B-A
        h = A
    elif niveau < niveauMax:
        return 0
        


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