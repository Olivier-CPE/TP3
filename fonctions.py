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
    On récupère le dictionnaire de mots, on le découpe en liste de mots, et on ne garde que les mots de 5 lettres ou
    plus
    """
    fichier = open("assets/dictionnaire.txt", "r")
    temp = fichier.read()
    fichier.close()
    dico_mots = temp.split()
    return [mot for mot in dico_mots if len(mot) >= 5]


def choisir_mot(dico_mots):
    """
    On choisit un mot au hasard dans le dictionnaire
    """
    n = rd.randint(0, len(dico_mots) - 1)
    mot = dico_mots[n]
    return mot


def mot_complet(lettre, mot_divise, lettres_essayees, liste_jeu):
    """
    On vérifie si la lettre est dans le mot, et on met à jour le jeu en cours
    """
    if lettre in lettres_essayees:
        return False, "Lettre déjà essayée"

    lettres_essayees.add(lettre)
    lettre_dans_mot = False

    for i, l in enumerate(mot_divise):
        if lettre == l:
            liste_jeu[i] = lettre.upper()
            lettre_dans_mot = True

    if lettre_dans_mot:
        return "".join(liste_jeu).lower() == "".join(mot_divise), "Lettre trouvée"
    else:
        return False, "Lettre non trouvée"


def afficher_jeu(liste_jeu):
    """
    On affiche le jeu en cours (liste de lettres)
    """
    return " ".join([lettre.upper() for lettre in liste_jeu if True])
