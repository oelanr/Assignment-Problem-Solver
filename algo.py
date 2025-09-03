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
        print(f"Start:A:{A} | A_prime:{A_prime}\n")
        
        if list_base == []:
            list_base = get_list_base(mat)
            
        A.append(A_prime.pop(A_prime.index(step_one(list_base))))

        print(f"Step1: liste_base:{list_base} | A:{A} | A_prime:{A_prime}\n")

        min_val,r = step_two(mat,A,A_prime,list_base)
        print(f"Step2: minimum:{min_val} | r: ligne {r+1}\n")
        show(mat)

        mat = step_three(mat,A,min_val)
        print(f"Step3:Augmenter de {min_val} tous les éléments de A={A}\n")
        show(mat)
        
        i_d,d = step_four(mat,A,r)
        print(f"Souligner par des tirets l'élément {d} de colonne {i_d+1} de ligne {r+1}")
        
        
        # Step 5
        if i_d in list_base:
            print(f"la colonne {i_d+1} contient d'autres bases. A:{A} | A_prime:{A_prime} .Retour à l'étape 2\n")
            j = 0
            while i_d in list_base and j<2:
                A.append(i_d)
                A_prime.remove(i_d)
                print(f"INFO:liste_base:{list_base} | A:{A} | A_prime:{A_prime}\n")
                min_val,r = step_two(mat,A,A_prime,list_base)
                print(f"Step2:minimum:{min_val} | r:ligne {r+1}\n")
                show(mat)

                mat = step_three(mat,A,min_val)
                print(f"Step3:Augmenter de {min_val} tous les éléments de A={A}\n")

                i_d,d = step_four(mat,A,r)
                print(f"Souligner par des tirets l'élément {d} de colonne {i_d+1} de ligne {r+1}")
                if i_d in list_base:
                    pass
                    print(f"La colonne {i_d+1} contient d'autres bases\n")
                j+=1
        else:
                print(f"la colonne {i_d+1} ne contient pas d'autres bases\n")

        
        list_base = step_six_seven(list_base,i_d,r)
        print(f"Etat de la base:{list_base}")
        
        print(f"***************************itération {t}*******************************************")
        t += 1

    if t > max_iter:
        print("Limite d'itérations atteinte, algo pas terminé correctement.")

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
    
    print(f"a:{a} | b:{b}\n")
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
