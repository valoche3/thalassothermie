import math
import heapq

def distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)


# Coordonnées des bâtiments (j'ai pris la thalassothermie au centre)
batiments = {
    "Thalassothermie": (0, 0),
    "LOT 8": (45, 111.25),
    "LOT 10": (35, 67.5),
    "LOT 19": (22.5, 2.5),
    "LOT 18": (-56.25, 6.25),
    "LOT COFESI": (42.5, 85)
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
    # on prend que les sommets dont on a besoin dans notre étude
    graphe_filtre = [
        (poids, a, b) for poids, a, b in graphe
        if a in batiments_utilises and b in batiments_utilises
    ]
   
    graphe_filtre.sort() # tri des arêtes par poids croissant
    
    parents = {b: b for b in batiments_utilises}

    def find(b):
        if parents[b] != b:
            parents[b] = find(parents[b])
        return parents[b]

    def union(b1, b2):
        parents[find(b1)] = find(b2)
    mst = []
    for poids, a, b in graphe_filtre:
        if find(a) != find(b):
            union(a, b)
            mst.append((a, b, poids))
    return mst


def connecter_batiments(noms_batiments):
    graphe = construire_graphe(batiments)
    mst = minimiser(graphe, noms_batiments)
    return mst



noms_a_connecter = ["Thalassothermie", "LOT 19", "LOT 8", "LOT COFESI", "LOT 10"]
arbre_minimal = connecter_batiments(noms_a_connecter)
print("Connexions minimales:")
for a, b, poids in arbre_minimal:
    print(f"{a} <-> {b}, Distance: {poids:.2f}")



