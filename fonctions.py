## Olivier et Maxime 


import random as rd

def recuperer_dictionnaire():
    """
        On recupère un fichier de mots on en fait une liste 
    """
    fichier = open("assets\dictionnaire.txt", "r")
    temp = fichier.read()
    dico_mots = temp.split()
    # conserve uniquement les mots de 5 lettres ou plus 
    return [mot for mot in dico_mots if len(mot) >= 5]
    

dictionnaire = recuperer_dictionnaire()


def choisir_mot(dico_mots):
    # prend un mot aléatoirement dans une liste de mots
    n = rd.randint(0, len(dico_mots) - 1)
    mot = dico_mots[n]
    return mot

print(choisir_mot(dico_mots=dictionnaire))