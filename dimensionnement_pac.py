def dimensionner_pompe_a_chaleur_reversible(surface_bureaux, charge_thermique_hiver, charge_thermique_ete, heures_occupation_par_jour, jours_occupation_par_semaine, facteur_securite=1.2):
    """
    Fonction pour dimensionner la pompe à chaleur réversible en fonction des besoins en chauffage (hiver) et en climatisation (été),
    ainsi que des heures d'occupation.
    
    Paramètres :
    surface_bureaux (float) : Surface des bureaux en m².
    charge_thermique_hiver (float) : Charge thermique estimée en W/m² pendant l'hiver (chauffage).
    charge_thermique_ete (float) : Charge thermique estimée en W/m² pendant l'été (climatisation).
    heures_occupation_par_jour (float) : Nombre d'heures d'occupation par jour.
    jours_occupation_par_semaine (float) : Nombre de jours d'occupation par semaine.
    facteur_securite (float) : Facteur de sécurité pour tenir compte des variations des besoins. Par défaut 1.2.
    
    Retourne :
    puissance_pompe (float) : Puissance estimée de la pompe à chaleur en kW.
    """
    
    # Charge thermique hivernale journalière
    charge_thermique_hiver_journaliere = surface_bureaux * charge_thermique_hiver * heures_occupation_par_jour
    # Charge thermique estivale journalière
    charge_thermique_ete_journaliere = surface_bureaux * charge_thermique_ete * heures_occupation_par_jour
    
    # Charge thermique hebdomadaire pour chaque saison
    charge_thermique_hiver_semaine = charge_thermique_hiver_journaliere * jours_occupation_par_semaine
    charge_thermique_ete_semaine = charge_thermique_ete_journaliere * jours_occupation_par_semaine
    
    # Application du facteur de sécurité
    charge_thermique_hiver_semaine_avec_securite = charge_thermique_hiver_semaine * facteur_securite
    charge_thermique_ete_semaine_avec_securite = charge_thermique_ete_semaine * facteur_securite
    
    # Conversion de la puissance en kW (1 kW = 1000 W)
    puissance_hiver_kW = charge_thermique_hiver_semaine_avec_securite / 1000
    puissance_ete_kW = charge_thermique_ete_semaine_avec_securite / 1000
    
    # La pompe à chaleur doit être dimensionnée en fonction de la charge thermique maximale
    puissance_pompe = max(puissance_hiver_kW, puissance_ete_kW)
    
    return puissance_pompe

# Exemple d'utilisation :
surface_bureaux = float(input("Entrez la surface des bureaux en m² : "))
charge_thermique_hiver = float(input("Entrez la charge thermique estimée en W/m² pour l'hiver (chauffage) : "))
charge_thermique_ete = float(input("Entrez la charge thermique estimée en W/m² pour l'été (climatisation) : "))
heures_occupation_par_jour = float(input("Entrez le nombre d'heures d'occupation par jour : "))
jours_occupation_par_semaine = float(input("Entrez le nombre de jours d'occupation par semaine (ex: 5 jours) : "))

# Calcul de la puissance nécessaire
puissance = dimensionner_pompe_a_chaleur_reversible(surface_bureaux, charge_thermique_hiver, charge_thermique_ete, heures_occupation_par_jour, jours_occupation_par_semaine)

print(f"La puissance estimée de la pompe à chaleur réversible est de : {puissance:.2f} kW")