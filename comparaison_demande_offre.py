import puissance
import numpy as np
import matplotlib.pyplot as plt

def temperature_ext(t, T):
    return 20*np.sin(2*np.pi*t/T - np.pi/2) + 18.25 + 273

def puissance_necessaire(T_voulue, T_ext, batiments):
    S = 0
    for _, volume, R in batiments:
        S += volume*np.abs(T_ext - T_voulue)/R
    return S

T = 365 * 24 * 3600
T_ed = 288
T_voulue = 296
c_ed = 4185
c_em = 4185
efficacite = 0.7
D_m = 6
P_el = 8550
batiments = #liste des infos des bâtiments
X = np.linspace(0, T, 100000)
X_mer = temperature_mer(X,T)
X_ext = temperature_ext(X, T)
Y = temperature_sortie(T_ed, X_mer, c_ed, c_em, efficacite)
Z = puissance_chaleur_sortie_pac(P_el, T_ed, Y, c_ed, c_em, D_m, efficacite)
W = puissance_necessaire(T_voulue, X_ext, batiments)
plt.plot(X,Z, label = "Puissance thermique produite en fonctionnement de chauffage")
plt.plot(X, W, label = "Puissance nécessaire au chauffage du parc de bâtiments")
plt.xlabel("Date en s")
plt.ylabel("Puissance en W")
plt.show()

