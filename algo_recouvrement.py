import math

def distance(coord1, coord2):
    """Calcule la distance euclidienne entre deux points."""
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)


# Coordonnées des bâtiments
batiments = {
    "Thalassothermie": (0, 0),
    "Lot 8": (45, 111.25),
    "Lot 18": (-56.25, 6.25),
    "Lot 10": (35, 67.5),
    "Lot COFESI (8 bis)": (42.5, 85),
    "Lot 19": (22.5, 2.5),
    "Lot C.L.E (14)": (-30, 80),
    "Lot FIRST (12)": (-58.75, 72.5),
    "Lot 4": (7.5, 176.25),
    "Lot 7": (3.75, 156.25),
    "Lot 6": (22.5, 150),
    "Lot 3 (CARUSO) / Lot 5 bis": (52.5, 165),
    "Lot DOCKERS (11)": (23, 37.5),
    "Lot 13": (-6.25, 43.75)
}


def construire_graphe(batiments):
    graphe = []
    noms = list(batiments.keys())
    for i in range(len(noms)):
        for j in range(i + 1, len(noms)):
            nom1, nom2 = noms[i], noms[j]
            dist = distance(batiments[nom1], batiments[nom2])
            graphe.append((dist, nom1, nom2))
    return graphe


def minimiser(graphe, batiments_utilises):
    graphe_filtre = [
        (poids, a, b) for poids, a, b in graphe
        if a in batiments_utilises and b in batiments_utilises
    ]
   
    graphe_filtre.sort()  # Tri par poids croissant
    
    parents = {b: b for b in batiments_utilises}

    def find(b):
        if parents[b] != b:
            parents[b] = find(parents[b])
        return parents[b]

    def union(b1, b2):
        parents[find(b1)] = find(b2)
    
    mst = []
    total_distance = 0  # Initialiser la somme des distances
    for poids, a, b in graphe_filtre:
        if find(a) != find(b):
            union(a, b)
            mst.append((a, b, poids))
            total_distance += poids  # Ajouter la distance à la somme totale
    return mst, total_distance


def connecter_batiments(noms_batiments):
    graphe = construire_graphe(batiments)
    mst, total_distance = minimiser(graphe, noms_batiments)
    return mst, total_distance


noms_a_connecter = list(batiments.keys())
arbre_minimal, somme_distances = connecter_batiments(noms_a_connecter)

print("Connexions minimales:")
for a, b, poids in arbre_minimal:
    print(f"{a} <-> {b}, Distance: {poids:.2f}")

print(f"\nSomme totale des distances: {somme_distances:.2f}")

print(f"Volume d'eau minimal : {somme_distances * 3.14 * (0.15**2):.2f} m^3")
