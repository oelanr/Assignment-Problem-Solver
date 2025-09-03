def show(mat):
    """Pour l'affichage de la matrice"""
    for l in mat:
        for c in l:
            print(f"{c:5}",end="")
        print()
    print()

def duplicate(mat):
    """Crée une copie superficielle d'une matrice."""
    return [row[:] for row in mat]
