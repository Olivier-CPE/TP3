# -*- coding: utf-8 -*-

"""
 * @author : maxime et olivier
 * @email : maxime.barthomeuf@cpe.fr
 * @date : 05/10/2023, jeudi
 * TODO :

 Fonctions du programme
 """

import random as rd


def recuperer_dictionnaire():
    """
        On recupère un fichier de mots on en fait une liste 
    """
    fichier = open("assets\dictionnaire.txt", "r")
    temp = fichier.read()
    fichier.close()
    dico_mots = temp.split()
    # conserve uniquement les mots de 5 lettres ou plus 
    return [mot for mot in dico_mots if len(mot) >= 5]
    

def choisir_mot(dico_mots):
    # prend un mot aléatoirement dans une liste de mots
    n = rd.randint(0, len(dico_mots) - 1)
    mot = dico_mots[n]
    return mot

def diviser_mot(mot):
    return list(mot)

def afficher_jeu(espace_reponse):
    return " ".join([lettre.upper() for lettre in espace_reponse if True])