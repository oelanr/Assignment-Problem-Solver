def show(mat):
    #Pour l'affichage de la matrice
    for l in mat:
        for c in l:
            print(f"{c:5}",end="")
        print()
    print()
        
def duplicate(mat):
    #Besoin de duplicat faute de matrice changé au cours du programme
    m = []
    
    for el in mat:
        t = []
        for i in el:
            t.append(i)
        m.append(t)
        
    return(m)   
        
def start(mat):
    #initialisation A:[] | A_prime:[0,1,2...,n]
    return [],[i for i in range(len(mat))]

def get_list_base(mat):
    #pour obtenir l'emplacement actuel de chaque minimum dans la matrice
    m = []
    for l in mat:
        m.append(l.index(min(l)))
    return m

def step_one(m):    
    #la colonne la plus récurrente dans le tableau contenant la liste des minimum (base|element souligné)
    return max(m,key=m.count)
    
def step_two(mat,A,A_prime,b):
    
    #b:recupérer les différents éléments souligné correspondant aux colonnes contenu dans A
    b = [l[b] if b in A else None for b,l in zip(b,mat)]
    
    #a:récupérer les différents éléments non souligné correspondant aux colonnes contenu dans A_prime 
    a = [[l[i] for i in A_prime] for l in mat]
    #puis filtrer pour récupérer chaque element minimum
    a= [min(i) if i != None else None for i in a ]
    #enfin faire le calcul de différence entre a et b
    r = [a_i - b_i  if a_i != None and b_i != None else float('inf') for a_i,b_i in zip(a,b)]
    
    print(f"a:{a} | b:{b}\n")
    return min(r),r.index(min(r))

def step_three(mat,A,m):
    #pour augmenter de m chaque element des colonnes contenu dans A
    for el in A:
        for i in range(len(mat)):
            mat[i][el] += m
    return mat

def step_four(mat,A,r):
    #souligner d'un trait l'element minimum ne se trouvant pas dans A et à la ligne r
    a = [mat[r][i] if i not in A else float('inf') for i in range(len(mat[r]))]
    return a.index(min(a)),min(a)

def step_six_seven(l_base,i_d,r):
    #mettre à jour la liste contenant les colonnes 
    l_base[r] = i_d
    return l_base

def calcul(mat,l_base):
    #pour calculer le temps optimal
    m = [l[i] for l,i in zip(mat,l_base)]
    
    return sum(m)