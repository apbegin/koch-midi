__author__ = 'Jonathan Jackson & Antoine Proulx-Bégin'

from math import trunc
import struct


# retourne distance horizontal entre p1 et p2
def __dist(p1, p2):
    return (p2[0] - p1[0])


def __fraction_distance(p1, p2, fraction):
    #Fonction qui retourne les coordonnees d'un point se trouvant a une
    #certaine fraction de la distance entre deux points
    vect_points = [p2[0]-p1[0], p2[1]-p1[1]]   #Vecteur de distantce entre p1 et p2
    new_point = [p1[0] + fraction * vect_points[0],
                 p1[1] + fraction * vect_points[1]]   #Nouveau point = p1 + fraction distance p2-1
    
    return new_point

def __genere_points(p1, p2, n):
    #fonction qui prend deux points et retourne 4 points selon de sorte
    #a faire un fractal de koch [p1--p3--p4--p5--p2} OU [A--C--D--E--B}
    p3 = __fraction_distance(p1, p2, 1/3)    #point C (ou p3) est sur la la droite AB
    p4 = __fraction_distance(p1, p2, 1/2)    #point D (ou p5) est sur la la droite AB
    p4[1] = trunc(p4[1] + 48/(2**n))                        #ajuste la hauteur de D selon trunct
    p5 = __fraction_distance(p1, p2, 2/3)    #point E (ou p5) est sur la la droite AB
    return [p1, p3, p4, p5, p2]
 
def __musique(A, B, niveau, niveauMax):
  
    next_points = __genere_points(A, B, niveau)
    if niveau == niveauMax:
        return [round(A[1]), (round(__dist(A, B)))] #on retourne la hauteur de A et la dist AB
    else:
        return [] + __musique(next_points[0], next_points[1], niveau+1, niveauMax)+\
               __musique(next_points[1], next_points[2], niveau+1, niveauMax) +\
               __musique(next_points[2], next_points[3], niveau+1, niveauMax) +\
               __musique(next_points[3], next_points[4], niveau+1, niveauMax)

def __generer_midi(koch_values):
    # Genere le fichier les données du fichier midi
    # Ecrit les donnes dans un fichier
    
    lst_note = []
    channel = 0x90
    volume = 0x60
    
    dist_index = trunc(len(koch_values)/2)
    
    #determine le temps d'un évenement  
    for x in range(dist_index-1):
        encoding_time = 0x00
        if koch_values[2*x+1] <= 127:
            encoding_time=0x80
            
        elif koch_values[2*x+1] <= 254:
            encoding_time=0x81
            koch_values[2*x+1]=koch_values[2*x+1]-127
            
        elif koch_values[2*x+1] >254:
            
            koch_values[2*x+1]=koch_values[2*x+1]-254
            encoding_time = 0x82
            
        lst_note.append([encoding_time,koch_values[2*x+1],channel,koch_values[2*x],volume])
        
    #nb de note x 5 pour le nombre de byte + 4 byte de la section F 
    track_length = len(lst_note)*5 + 4
    
    
    midiHeader =[0x4d, 0x54,0x68, 0x64 ,0x00, 0x00, 0x00,0x06, 0x00,
                0x00, 0x00, 0x01, 0x00, 0x80, 0x4d, 0x54, 0x72, 0x6b]
    
    f = open('musique.mid','wb')
    f.truncate()
    
    f.write(bytearray(midiHeader))
    f.write(struct.pack('>I',track_length))
    
    for x in range(len(lst_note)):
        track_buffer = bytearray(5)
        struct.pack_into('>5B',track_buffer,0,lst_note[x][0],lst_note[x][1],
                         lst_note[x][2],lst_note[x][3],lst_note[x][4])
        f.write(track_buffer)
    
    #indique la fin de la track
    f.write(struct.pack('>2h',0x00FF,0x2F00))
    f.close()
    
a = [0, 36]
b = [77760, 36]

__generer_midi(__musique(a, b, 0, 5))
