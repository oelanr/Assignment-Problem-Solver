from utils.matrice import duplicate, show

def macks_bradford(matrice_initiale):
    """
    Fonction principale (retourne le coût optimal)
    """
    mat = duplicate(matrice_initiale)
    mat_copy = duplicate(matrice_initiale)
    
    list_base = []
    t = 1
    # Limite de sécurité pour éviter une boucle infinie.
    max_iter = len(mat) * 5 

    while t<max_iter:
        A,A_prime = start(mat)
        
        if list_base == []:
            list_base = get_list_base(mat)
            
        A.append(A_prime.pop(A_prime.index(step_one(list_base))))
        min_val,r = step_two(mat,A,A_prime,list_base)
        mat = step_three(mat,A,min_val)
        
        i_d,d = step_four(mat,A,r)
        # Step 5
        if i_d in list_base:
            j = 0
            while i_d in list_base and j<2:
                A.append(i_d)
                A_prime.remove(i_d)
                min_val,r = step_two(mat,A,A_prime,list_base)

                mat = step_three(mat,A,min_val)

                i_d,d = step_four(mat,A,r)
                if i_d in list_base:
                    pass
                j+=1

        
        list_base = step_six_seven(list_base,i_d,r)
        
        t += 1

    cout_optimal = calcul(mat_copy,list_base)
    
    return cout_optimal, list_base

def start(mat):
  #  initialisation A:[] | A_prime:[0,1,2...,n]
    return [],[i for i in range(len(mat))]

def get_list_base(mat):
   # pour obtenir l'emplacement actuel de chaque minimum dans la matrice
    m = []
    for l in mat:
        m.append(l.index(min(l)))
    return m

def step_one(m):    
   #  la colonne la plus récurrente dans le tableau contenant la liste des minimum (base|element souligné)
    return max(m,key=m.count)
    
def step_two(mat,A,A_prime,b):
    
    #b:recupérer les différents éléments souligné correspondant aux colonnes contenu dans A
    b = [l[b] if b in A else None for b,l in zip(b,mat)]
    
    #a:récupérer les différents éléments non souligné correspondant aux colonnes contenu dans A_prime 
    a = [[l[i] for i in A_prime] for l in mat]
    #puis filtrer pour récupérer chaque element minimum
    a= [min(i) if i else None for i in a ]
    
    #calcul de différence entre a et b
    r = [a_i - b_i  if a_i != None and b_i != None else float('inf') for a_i,b_i in zip(a,b)]
    
    min_val = min(r)
    return min_val,r.index(min_val)

def step_three(mat,A,m):
    #pour augmenter de m chaque element des colonnes contenu dans A
    
    if (m == 0) :
        pass
        #print("Augmentation de 0 donc aucun changement")

    for elem in A:
        for i in range(len(mat)):
            mat[i][elem] += m
            
    return mat

def step_four(mat,A,r):
    #souligner de tirets l'element minimum ne se trouvant pas dans A et à la ligne r
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
