import numpy as np
from scipy.integrate import quad 

def calcul_charge_thermique(T_int, T_ext, R, G_solaire, F_solaire):
    """
    Calcule la charge thermique nécessaire pour climatiser une pièce.
    
    Paramètres :
    - T_int : Température intérieure souhaitée (°C)
    - T_ext : Température extérieure (°C)
    - R : Résistance thermique des murs (m².K/W)
    
    Retour :
    - Charge thermique nécessaire en watts (W)
    """
    # Charge thermique liée aux murs
    Ps_murs = (T_ext - T_int) / R
    
    # Charge thermique solaire : Gain solaire sur la surface vitrée
    Ps_solaire = G_solaire * F_solaire
    return (Ps_murs, Ps_solaire)

def charge_thermique_ete_avec_surface(T_int, T_ext, R, G_solaire, F_solaire, surface_bureaux, surface_vitree):
    Ps_murs, Ps_solaire = calcul_charge_thermique(T_int, T_ext, R, G_solaire, F_solaire)
    return abs(surface_bureaux * Ps_murs + Ps_solaire * surface_vitree)

def charge_thermique_hiver_avec_surface(T_int, T_ext, R, G_solaire, F_solaire, surface_bureaux, surface_vitree):
    Ps_murs, Ps_solaire = calcul_charge_thermique(T_int, T_ext, R, G_solaire, F_solaire)
    return abs(surface_bureaux * Ps_murs - Ps_solaire * surface_vitree)

def dimensionner_pompe_a_chaleur_reversible(surface_bureaux, surface_vitree, charge_thermique_hiver, charge_thermique_ete, facteur_securite=1.2):
    """
    Fonction pour dimensionner la pompe à chaleur réversible en fonction des besoins en chauffage (hiver) et en climatisation (été),
    ainsi que des heures d'occupation.
    
    Paramètres :
    surface_bureaux (float) : Surface des bureaux en m².
    charge_thermique_hiver (float) : Charge thermique estimée en W/m² pendant l'hiver (chauffage).
    charge_thermique_ete (float) : Charge thermique estimée en W/m² pendant l'été (climatisation).
    facteur_securite (float) : Facteur de sécurité pour tenir compte des variations des besoins. Par défaut 1.2.
    
    Retourne :
    puissance_pompe (float) : Puissance estimée de la pompe à chaleur en kW.
    """
    Ps_mursh, Ps_solaireh = charge_thermique_hiver
    # Charge thermique hivernale
    charge_thermique_hiver_total = abs(surface_bureaux * Ps_mursh - Ps_solaireh * surface_vitree)
    Ps_murse, Ps_solairee = charge_thermique_ete
    # Charge thermique estivale
    charge_thermique_ete_total = abs(surface_bureaux * Ps_murse + Ps_solairee * surface_vitree)
    
    # Application du facteur de sécurité
    charge_thermique_hiver_semaine_avec_securite = charge_thermique_hiver_total * facteur_securite
    charge_thermique_ete_semaine_avec_securite = charge_thermique_ete_total * facteur_securite
    
    # Conversion de la puissance en kW (1 kW = 1000 W)
    puissance_hiver = charge_thermique_hiver_semaine_avec_securite
    puissance_ete = charge_thermique_ete_semaine_avec_securite
    
    # La pompe à chaleur doit être dimensionnée en fonction de la charge thermique maximale
    puissance_pompe = (puissance_hiver + puissance_ete + abs(puissance_hiver - puissance_ete))/2 
    
    return puissance_pompe

def temperature_ext(T, t):
    return 20*np.sin(2*np.pi*t/T - np.pi/2) + 18.25 + 273

surface_bureaux = float(input("Entrez la surface des bureaux en m² : "))
surface_vitree = float(input("Entrez la surface vitrée en m² :"))
R = 4
T = 365 * 24 * 3600  # Une année en secondes
T_int = 21 + 273  # Température intérieure souhaitée en Kelvin


def facteur_charge(periode):
    I_p, _ = quad(lambda t: dimensionner_pompe_a_chaleur_reversible(surface_bureaux, surface_vitree, calcul_charge_thermique(T_int, temperature_ext(T, t), R, 350, 0.7), calcul_charge_thermique(T_int, temperature_ext(T, t), R, 750, 0.7)), 0, periode)
    return (I_p/(443300*periode))

print(facteur_charge(T))