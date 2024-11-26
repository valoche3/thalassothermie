from puissance import *
import numpy as np
import matplotlib.pyplot as plt
from math import *
from estimation_potentiel import *



for i in range(12):
    print(batiment[0])


def recuperer_donnees():
    nombre_batiment = int(input('quel est le nombre de bâtiments considérés ?'))

    batiment = [(0,0,0) for i in range(nombre_batiment)]

    #type_batiment = [O for i in range(nombre_batiment)] #type de batiment --> deuxième étape
    surface_totale = [0 for i in range(nombre_batiment)] #surfaces utiles pour calculer les pertes
    K = [0 for i in range(nombre_batiment)]

    for i in range(nombre_batiment):

        #on récupère le nom du bâtiment
        while True:
            try:
                nom = input(f'quel est le nom du batiment {i} ?')
                break
            except ValueError:
                print('donnée invalide ! réessayez')
            
        #on récupère les coefficients de perte
        while True:
            try:
                R = float(input(f'quel est le coefficient de perte du batiment {nom} ?'))
                break
            except ValueError:
                print('donnée invalide ! réessayez')
        K[i] = 1/R
    
    #on récupère la surface du batiment
        while True:
            try:
                surface_sol = float(input(f'quelle est la surface au sol du batiment {nom} ?'))
                break
            except ValueError:
                print('donnée invalide ! réessayez')

        #on récupère la hauteur du batiment
        while True:
            try:
                hauteur_typique = float(input(f'quelle est la hauteur typique du batiment {nom} ?'))
                break
            except ValueError:
                print('donnée invalide ! réessayez')

        #on calcule la longueur typique puis la surface latérale
        longueur_typique = sqrt(surface_sol)

        #on calcule la surface totale utile pour le calcul des pertes
        surface_totale[i] = 2*surface_sol + 4*longueur_typique*hauteur_typique

        #on met tout ça dans la liste batiment
        batiment[i] = (nom,surface_totale[i],K[i])

    return batiment


def temperature_ext(t, T):
    return 20*np.sin(2*np.pi*t/T - np.pi/2) + 18.25 + 273

def puissance_necessaire(T_voulue, T_ext, batiments):
    S = 0
    for _, surface, R in batiments:
        S += surface*np.abs(T_ext - T_voulue)/R
    return S

# +
T = 365 * 24 * 3600 #le nombre de seconde dans l'année
T_ed = 288 
T_voulue = 296
c_ed = 4185
c_em = 4185
efficacite = 0.7
D_m = 6
P_el = 8550

batiments = recuperer_donnees()

#batiments = [("Lot 8", 1613, 4), ("Lot 10", 585.56, 4), ("Lot COFESI", 1382.4, 4), ("Lot 19", 132.48, 4), ("LotC.L.E", 1981.44, 4), ("Lot FIRST", 3237.12, 4), ("Lot 4", 581.76, 4), ("Lot 7", 336, 4), ("Lot 6", 225, 4), ("Lot 3", 118.75, 4), ("Lot DOCKERS", 162, 4), ("Lot 13", 243, 4)]
X = np.linspace(0,T, 100000)

X_mer = temperature_mer(X,T)
X_ext = temperature_ext(X, T)
Y = temperature_sortie(T_ed, X_mer, c_ed, c_em, efficacite)
Z = puissance_chaleur_sortie_pac(P_el, T_ed, Y, c_ed, c_em, D_m, efficacite)
W = puissance_necessaire(T_voulue, X_ext, batiments)
plt.figure(figsize = (10,6))
#plt.plot(X,Z, label = "Puissance thermique produite en fonctionnement de chauffage", color = 'red')
plt.plot(X, W, label = "Puissance nécessaire au chauffage du parc de bâtiments", color = 'blue')
plt.xlabel("Date en s")
plt.ylabel("Puissance en W")
plt.show()
# -


plt.plot(X,Z, label = "Puissance thermique produite en fonctionnement de chauffage", color = 'red')
plt.plot(X, W, label = "Puissance nécessaire au chauffage du parc de bâtiments", color = 'blue')
plt.xlabel("Date en s")
plt.ylabel("Puissance en W")
plt.show()


