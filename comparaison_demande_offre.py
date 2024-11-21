import puissance
import numpy as np
import matplotlib.pyplot as plt

nombre_batiment = int(input('quels est le nombre de bâtiments considérés ?'))

surface_batiment = [0 for i in range(nombre_batiment)]
hauteur_batiment = [0 for i in range(nombre_batiment)]
type_batiment = [0 for i in range(nombre_batiment)] #dans un second temps, calcul du coefficient de perte

for i in range(nombre_batiment):
    
    #on récupère la surface du bâtiment
    while True: #on veut forcément une donnée du type int
        try:
            surface = int(input(f'quelle est la surface du bâtiment {i+1} considéré en m2 ?'))
            break
        except ValueError:
            print("ce n'est pas un nombre valide ! réessayez ")
    surface_batiment[i] = surface

    #on récupère la hauteur du bâtiment
    while True: #on veut forcément une donnée du type int
        try:
            hauteur = int(input(f'quelle est la hauteur du bâtiment {i+1} considéré en m2 ?'))
            break
        except ValueError:
            print("ce n'est pas un nombre valide ! réessayez ")
    hauteur_batiment[i] = hauteur

volume_batiment = [0 for i in range(nombre_batiment)]

for i in range(nombre_batiment):
    volume_batiment[i] = surface_batiment[i]*hauteur_batiment[i]

#dans le cas où on construit un nouveau bâtiment, on a un coefficient R = 4 (façades) et 8 (toit)

valeurs_R = [0 for i in range(nombre_batiment)]
    
for i in range(nombre_batiment):
    while True: #on veut forcément une donnée du type int
        try:
            R = int(input(f"quelle est le coefficient d'isolation R du bâtiment {i+1} considéré en m2 ?"))
            break
        except ValueError:
            print("ce n'est pas un nombre valide ! réessayez ")
    valeurs_R[i] = R
    
valeurs_K = [0 for i in range(nombre_batiment)]

for i in range(nombre_batiment):
    valeurs_K[i] = 1/valeurs_R[i]

#on considère que la température idéale est de 22 degrés en été et de 24 degrés en hiver

#T_exterieur = int(input('quelle est la température extérieur en celcius ?')) #on pourra récupérer des données sur un an
#T_voulue = int(input('quelle est la température voulue dans le bâtiment en celcius ?'))

puissance_batiment = [0 for i in range(nombre_batiment)]

for i in range(nombre_batiment):
    puissance_batiment[i] = volume_batiment[i]*np.abs(T_exterieur - T_voulue)*valeurs_K[i]

valeur_puissance_totale = sum(puissance_batiment)

#T_exterieur = [8,8,10,13,17,21,23,24,20,17,12,9] #température par mois
#T_voulue = [24,24,24,24,22,22,22,22,22,22,24,24] #température par mois

puissance_batiment = [[0 for i in range(nombre_batiment)] for j in range(12)]

valeur_puissance_totale = [0 for j in range(12)]

for j in range(12):
    
    for i in range(nombre_batiment):
        puissance_batiment[j][i] = volume_batiment[i]*np.abs(T_exterieur[j] - T_voulue[j])*valeurs_K[i]

    valeur_puissance_totale[j] = sum(puissance_batiment[:][j])

def temperature_ext(t, T):
    

T = 365 * 24 * 3600
T_ed = 288
c_ed = 4185
c_em = 4185
efficacite = 0.7
D_m = 6
P_el = 8550
X = np.linspace(0,T, 100000)
X_2 = temperature_mer(X,T)
Y = temperature_sortie(T_ed, X_2, c_ed, c_em, efficacite)
Z = puissance_chaleur_sortie_pac(P_el, T_ed, Y, c_ed, c_em, D_m, efficacite)
plt.plot(X,Z, label = "Puissance thermique produite en fonctionnement de chauffage")
plt.xlabel("Date en s")
plt.ylabel("Puissance en W")
plt.show()

