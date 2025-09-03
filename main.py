from clean import macks_bradford
from utils.matrice import show

# La matrice peut être chargée d'un fichier ou définie ici
mat = [
    [44, 74, 35, 49, 30, 45],
    [22, 28, 42, 59, 83, 41],
    [28, 39, 54, 47, 35, 24],
    [49, 53, 45, 50, 43, 38],
    [27, 37, 30, 18, 30, 22],
    [70, 27, 21, 32, 31, 9]
]

# Appel simple à la fonction principale
cout, affectation = macks_bradford(mat)

# Affichage propre des résultats
print("Matrice initiale:")
show(mat)
print(f"Temps optimal : {cout}")
