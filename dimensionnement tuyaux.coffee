import math

def calcul_diametre_tuyau(params):
    """
    Calcule le diamètre interne nécessaire pour un tuyau transportant un fluide dans un réseau de thalassothermie.

    Arguments :
        params (dict) : Dictionnaire contenant les paramètres suivants :
            - 'puissance' (float) : Puissance de l'installation en watts (W).
            - 'delta_temp' (float) : Écart de température entre l'entrée et la sortie (en °C ou K).
            - 'vitesse' (float) : Vitesse de l'eau dans le tuyau (en m/s).

    Retourne :
        float : Diamètre interne du tuyau en mètres (m).
    """
    # Constantes pour l'eau
    cp = 4180  # Capacité thermique massique de l'eau en J/(kg·K)
    rho = 1000  # Densité de l'eau en kg/m³

    # Extraction des paramètres depuis le dictionnaire
    puissance = params.get('puissance')
    delta_temp = params.get('delta_temp')
    vitesse = params.get('vitesse')

    # Validation des paramètres
    if not puissance or not delta_temp or not vitesse:
        raise ValueError("Les paramètres 'puissance', 'delta_temp' et 'vitesse' doivent être renseignés.")

    # Calcul du débit volumique (m³/s)
    debit_volumique = puissance / (cp * delta_temp * rho)

    # Calcul du diamètre intérieur (m)
    diametre = math.sqrt((4 * debit_volumique) / (math.pi * vitesse))

    return diametre

# Exemple d'utilisation
params = {
    'puissance': 100000,  # 100 kW
    'delta_temp': 5,      # 5 °C
    'vitesse': 2          # 2 m/s
}

diametre = calcul_diametre_tuyau(params)
print(f"Diamètre requis : {diametre:.3f} m")
