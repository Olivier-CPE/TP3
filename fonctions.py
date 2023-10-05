# -*- coding: utf-8 -*-

"""
 * @author : maxime et olivier
 * @email : maxime.barthomeuf@cpe.fr
 * @date : 05/10/2023, jeudi
 * TODO :

 Contient les fonctions du programme
"""


fichier = open("assets\dictionnaire.txt", "r")
temp = fichier.read()
dico_mots = temp.split()
print(dico_mots)
