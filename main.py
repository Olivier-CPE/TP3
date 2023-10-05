# -*- coding: utf-8 -*-

"""
 * @author : maxime et olivier
 * @email : maxime.barthomeuf@cpe.fr
 * @date : 05/10/2023, jeudi
 * TODO :

 Fonction principale du programme
"""
import fonctions as fct


def main():
    dictionnaire = fct.recuperer_dictionnaire()

    mot = fct.choisir_mot(dictionnaire)
    mot_divise = list(mot)

    # creation d'une variable reponse utilisateur avec initialisation de la premiere lettre
    liste_jeu = [mot_divise[0]]
    liste_jeu.extend(["_"] * (len(mot_divise) - 1))

    lettres_essayees = set()  # ensemble vide pour stocker les lettres déjà essayées

    max_tentatives = 8
    nb_tentatives = 0
    mot_trouve = False

    while not mot_trouve and nb_tentatives < max_tentatives:

        # Afficher l'état actuel du jeu
        print(f'\n{fct.afficher_jeu(liste_jeu)}')

        # Demander à l'utilisateur de choisir une lettre
        lettre = input("Choisir une lettre : ").lower()

        mot_complet, message = fct.mot_complet(lettre, mot_divise, lettres_essayees, liste_jeu)

        if mot_complet:
            mot_trouve = True
        else:
            print(message)
            nb_tentatives += 1

    if mot_trouve:
        print(f'\n{fct.afficher_jeu(liste_jeu)}')
        print('Bravo, vous avez trouvé le mot !')
    else:
        print('Dommage, vous avez perdu ! Le mot était :', mot)

    b = input("\nChoisir 'r' pour recommencer ou 'a' pour arrêter : ")

    if b == 'r':
        return main()
    else:
        print("Au revoir !")


if __name__ == "__main__":
    main()
