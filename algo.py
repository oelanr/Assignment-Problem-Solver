def show(mat):
    for l in mat:
        for c in l:
            print(f"{c:5}",end="")
        print()
    print()
        
def duplicate(mat):
    m = []
    
    for el in mat:
        t = []
        for i in el:
            t.append(i)
        m.append(t)
        
    return(m)   
        
def start(mat):
    return [],[i for i in range(len(mat))]

def get_list_base(mat):
    m = []
    for l in mat:
        m.append(l.index(min(l)))
    return m

def step_one(m):    
    return max(m,key=m.count)
    
def step_two(mat,A,A_prime,b):
    b = [l[b] if b in A else None for b,l in zip(b,mat)]
     
    #A checker car la selection des non souligner ne marche pas correctement à cause du paramètre A_prime
    a = [[l[i] for i in A_prime] for l in mat]
    # a = [[l[i] for i in A_prime] if mat.index(l) not in A else None for l in mat]
    a= [min(i) if i != None else None for i in a ]
    r = [a_i - b_i  if a_i != None and b_i != None else float('inf') for a_i,b_i in zip(a,b)]
    
    print(f"a:{a} | b:{b}\n")
    return min(r),r.index(min(r))

def step_three(mat,A,m):
    for el in A:
        for i in range(len(mat)):
            mat[i][el] += m
    return mat

def step_four(mat,A,r):
    a = [mat[r][i] if i not in A else float('inf') for i in range(len(mat[r]))]
    return a.index(min(a)),min(a)

def step_six_seven(l_base,i_d,r):
    l_base[r] = i_d
    return l_base

def calcul(mat,l_base):
    m = [l[i] for l,i in zip(mat,l_base)]
    
    return sum(m)