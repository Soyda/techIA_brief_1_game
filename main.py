# import 
import fonction 
import random 

# Déclaration de nos variables 
degats = 8
my_hp = 50
round = 1
lvl = 1 
enemy_hp = 30
ennemy_degats = 5
prenom = input("Quel est votre prenom ?")
choix_principal = input("Menu principal : \n Quel est votre choix ? \n 1 - start  \n 2 - score \n 3 - quitter ")
choix_combat = input (f"Que voulez_vous faire {prenom}") 

# incrémentation des lvl up : 
if round % 3 == 0 :
    lvl += 1 

# commencement de la boucle : 
leave = True 
while leave : 