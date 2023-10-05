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
    liste_lettres = fct.diviser_mot(mot)
    
    # creation d'une variable reponse utilisateur avec initialisation de la premiere lettre
    espace_reponse = []
    
    for lettre in liste_lettres:
        if lettre == liste_lettres[0]:
            espace_reponse.append(lettre)
        else:
            espace_reponse.append("_")

    essais = set()
    mot_trouve = False
    nb = 0

    while not mot_trouve and nb < 8:
        print(fct.afficher_jeu(espace_reponse))
        entree_lettre = input("Choisir une lettre : ").lower()
        
        if entree_lettre in essais:
           print("Lettre déjà rentrée")
           
        elif not entree_lettre in espace_reponse:
            essais.add(entree_lettre)

            lettre_dans_mot = False
            
            for i, lettre in enumerate(liste_lettres):
                if entree_lettre == lettre:
                    espace_reponse[i] = lettre.upper()
                    lettre_dans_mot = True
                    
                    mot_trouve = "".join(espace_reponse).lower() == mot

            if not lettre_dans_mot:
                nb += 1

    
    if mot_trouve:
        print(fct.afficher_jeu(espace_reponse))
        print('Bravo')
    else:
        print("Trop d'essais, le mot était :", mot)

    b = input("Choisir 'r' pour recommencer ou 'a' pour arreter : ") 

    if b == 'r':
        return main()
    else :
        print("Au revoir !")     

    
                        
           

             










if __name__ == "__main__": 
    main()
