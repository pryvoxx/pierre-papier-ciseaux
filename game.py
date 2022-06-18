

##########################################
# Pierre, Papier, Ciseaux                # 
# Coded by pryvox                        #
# Github : https://github.com/pryvoxx    #
# discord : https://discord.gg/KfR2M88G  #
##########################################


# importer les modules nécaissaires 
import os 
import random 
from pystyle import Write, Colors, Colorate, Box 

# faire les couleurs 
purple = Colors.green 
latence = interval = 0.04

# installer le module nécaissaire 
print("INSTALLATION DU MODULE [*]")
os.system('pip install pystyle')

# clear le terminal 
os.system('cls')

# commencement du programme 
# fonction
def main():
    # presenter le jeu 
    print(purple, "PIERRE PAPIER CISEAUX")

    while True:

        # faire les choix 
        print(purple, "\n-1 Pierre\n-2 Papier\n-3 Ciseaux\n")

        # faire la demande a l'utilisateur 
        user = Write.Input("Que voulez vous choisir ->", purple, latence)

        # faire le bot qui va répondre a l'utilisateur 
        liste = ["Pierre", "Papier", "Ciseaux"]
        # tirer la liste au sort 
        afficher_liste = random.choice(liste)
        print(purple, "\nRobot : ", afficher_liste)

        # les conditions 
        # proposition 1
        if (user == '1' and afficher_liste == 'Pierre'): 
            print(purple, "\négalité")
        elif (user == '1' and afficher_liste == 'Papier'):
            print(purple, "\nVous avez perdu !")
        elif (user == '1' and afficher_liste == 'Ciseaux'):
            print(purple, "\nVous avez gagné !")
            
            
        # proposition 2 
        if (user == '2' and afficher_liste == 'Pierre'):
            print(purple, "\nVous avez gagné !")
        elif (user == '2' and afficher_liste == 'Papier'):
            print(purple, "\négalité !")
        elif (user == '2' and afficher_liste == 'Ciseaux'):
            print(purple, "\nVous avez perdu !")


        # propositions 3
        if (user == '3' and afficher_liste == 'Ciseaux'):
            print(purple, "\négalité !")
        elif (user == '3' and afficher_liste == 'Pierre'):
            print(purple, "\nVous avez perdu !")
        elif (user == '3' and afficher_liste == 'Papier'):
            print(purple, "\nVous avez gagné !")

if __name__=='__main__':
    main()
