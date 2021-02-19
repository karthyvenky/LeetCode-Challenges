#%%
def getdiag(mat,i,r,j,c):
    arr = []
    for x,y in zip(range(i,r),range(j,c)):
        arr.append(mat[x][y])
        #print(x,y)
    return arr

def setdiag(mat,arr,i,r,j,c):
    for x,y in zip(range(i,r),range(j,c)):
        mat[x][y] = arr.pop()


def diagonalsort(mat):
    r,c = len(mat), len(mat[0])
    print(mat)
    for i in range(r):
        arr = getdiag(mat, i,r,0,c)
        arr.sort(reverse=True)
        setdiag(mat,arr,i,r,0,c)
    for j in range(1,c):
        arr = getdiag(mat,0,r,j,c)
        arr.sort(reverse= True)
        setdiag(mat,arr,0,r,j,c)
    print(mat)
# %%
mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
diagonalsort(mat)
# %%
