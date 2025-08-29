from algo import *

#For test
# mat = [
#     [10,  5, 9, 18, 11],
#     [13, 19, 6, 12, 14],
#     [ 3,  2, 4,  4,  5],
#     [18,  9,12, 17, 15],
#     [11,  6,14, 19, 10],
# ]

# mat = [
#     [ 4,  6,  9,  7],
#     [13, 10, 14, 14],
#     [ 9,  9, 16, 13],
#     [12, 10, 12, 10],
# ]

mat = [
    [ 9, 20, 60, 15, 21],
    [38, 71, 69, 49, 60],
    [28, 13, 80, 28, 34],
    [58, 34, 13, 37, 25],
    [39,  3, 53, 20, 21],
]

cp = duplicate(mat)

l_base = []
t = 1
while 1:
    A,A_prime = start(mat)
    print(f"Start:A:{A} | A_prime:{A_prime}\n")
    
    if l_base == []:
        l_base = get_list_base(mat) # s'execute une fois seulement sinon l_base sera toujours mis à jour à chaque itération
        
    A.append(A_prime.pop(A_prime.index(step_one(l_base))))
    print(f"Step1:liste_base:{l_base} | A:{A} | A_prime:{A_prime}\n")

    m,r = step_two(mat,A,A_prime,l_base)
    print(f"Step2:minimum:{m} | r:ligne {r+1}\n")
    show(mat)

    mat = step_three(mat,A,m)
    print(f"Step3:Augmenter de {m} tous les éléments de A={A}\n")

    i_d,d = step_four(mat,A,r)
    print(f"Souligner par des tirets l'élément {d} de colonne {i_d+1} de ligne {r+1}")
    
    if i_d in l_base:
        #vérifier si il n'y a pas d'autre base
        print(f"la colonne {i_d+1} contient d'autre base. A:{A} | A_prime:{A_prime} .REVENIR A L'ETAPE 2\n")
        j = 0
        while i_d in l_base and j<2:
            A.append(i_d)
            A_prime.remove(i_d)
            print(f"INFO:liste_base:{l_base} | A:{A} | A_prime:{A_prime}\n")
            m,r = step_two(mat,A,A_prime,l_base)
            print(f"Step2:minimum:{m} | r:ligne {r+1}\n")
            show(mat)

            mat = step_three(mat,A,m)
            print(f"Step3:Augmenter de {m} tous les éléments de A={A}\n")

            i_d,d = step_four(mat,A,r)
            print(f"Souligner par des tirets l'élément {d} de colonne {i_d+1} de ligne {r+1}")
            if i_d in l_base:
                print(f"La colonne {i_d+1} contient d'autre base\n")
            j+=1
                
    else:
        print(f"la colonne {i_d+1} ne contient pas d'autre base\n")
    l_base = step_six_seven(l_base,i_d,r)
    print(f"Etat de la base:{l_base}")
    
    if len(l_base) == len(set(l_base)):
        print("OK")
        break
    t+=1
    print(f"***************************itération {t}*******************************************")
    
print("***********************Résultat**************************")
show(cp)
print(f"Temps optimal :{calcul(cp,l_base)}")