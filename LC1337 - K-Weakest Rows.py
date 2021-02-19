def kweakest(mat, k): #fastest
    d = {}
    for i,j in enumerate(mat):
        d[i] = sum(j)

    return(sorted(d,key=d.get)[:k])

def kweakestnumpy(mat,k): #slower
    return(list(np.argsort(np.sum(mat, axis = 1), kind='mergesort')[:k]))
    
    
    