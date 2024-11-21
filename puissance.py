import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def temperature_sortie(T_ed, T_em, c_ed, c_em, efficacite): # calcul la température de l'eau douce en sortie d'échangeur
    return efficacite*(c_em*T_em + c_ed*T_ed)/(c_ed+c_em)

def puissance_chaleur_sortie_pac(P_el, T_ed, T_em, c_ed, c_em, D_m, efficacite): # calcul de la puissance thermique de sortie d'une pompe à chaleur
    return P_el+c_ed*D_m*temperature_sortie(T_ed, T_em, c_ed, c_em, efficacite)

def puissance_perdue_clim(P_el, T_ed, T_em, c_ed, c_em, D_m, efficacite): # calcul de la puissance thermique perdue par le bâti en fonctionnement clim
    return c_ed*D_m*temperature_sortie(T_ed, T_em, c_ed, c_em, efficacite) - P_el

def temperature_mer(t, T):
    return 5.45*np.sin(2*np.pi*t/T - np.pi/2) + 18.25

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
Z_2 = puissance_perdue_clim(P_el, T_ed, Y, c_ed, c_em, D_m, efficacite)
plt.plot(X,Z, label = "Puissance thermique produite en fonctionnement de chauffagr")
plt.plot(X, Z_2, label = "Puissance thermique pompée en fonctionnement climatiseur")
plt.xlabel("Date en s")
plt.ylabel("Puissance en W")
plt.show()





