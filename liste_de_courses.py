import sys
import os

fichier_liste = "fichier_listeeeee.txt"

def charger_liste():
    if os.path.exists(fichier_liste):
        with open(fichier_liste, "r") as f:
             return f.read().splitlines()
    else:
        return []
    
def sauvegarder_liste(liste):
    with open(fichier_liste, "w") as f:
        for element in liste:
            f.write(element + "\n")
            
liste = charger_liste()
separation = ("_")*15

while True:
    menus = int(input("""\nChoisissez parmi les options ci-dessous:\n""" + separation + "\n\n(1) Afficher la liste\n(2) Ajouter un élément à la liste\n(3) Retirer un élément de la liste\n(4) Supprimer la liste\n\n(5)Quitter\n""" + separation + "\n\nVotre choix : """))
    if menus == 1:
        if not liste:
            print("Votre liste est vide.\n" + separation)
        else:
            print(f"Votre liste contient les éléments suivants : {liste}.")
    if menus == 2:
        ajouter = input("\nQue souhaitez vous ajouter ?\n" + separation + "\nVotre choix: ")
        liste.append(ajouter)
        print(f"L'élément {ajouter} a bien été ajouté à la liste.")
    if menus == 3:
        retirer = input("\nQue souhaitez vous retirer ?\n" + separation + "\nVotre choix: ")
        liste.remove(retirer)
        print(f"L'élément {retirer} a bien été retiré de la liste.")
    if menus == 4:
        liste.clear()
        print(f"Votre liste a bien été supprimée {liste}.")
    if menus == 5:
        print(separation + "\n\nA bientôt! (｡◕‿‿◕｡)\n" + separation)
        sauvegarder_liste(liste)
        sys.exit()
        