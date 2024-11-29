from algo_recouvrement import connecter_batiments
noms_a_connecter = ["Thalassothermie", "LOT 19", "LOT 8", "LOT COFESI", "LOT 10"]

def cout(graphe, prix_au_metre):
    S = 0
    for a, b, poids in graphe:
        S+=poids
    return S*prix_au_metre

prix_metre = 800
arbre_minimal = connecter_batiments(noms_a_connecter)
print("Coût de l'installation de tuyauterie en euros")
print(cout(arbre_minimal, prix_metre)) 