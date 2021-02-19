#%%
#Subsequence 

def subsequence(string):
    if len(string) == 0:
        return " "
    parts = []
    for part in subsequence(string[1:]):
        parts.append(part)
        parts.append(string[0]+ part)
    return parts

# %%
subsequence("NET")
# %%
# Longest Common Subsequence - by recursion
def LCS_recursion(X,Y):
    if len(X) == 0 or len(Y) == 0:
        return 0
    for i in range(len(X)):
        for j in range(len(Y)):
            if X[i] == Y[j]:
                return 1 + LCS_recursion(X[i+1:], Y[j+1:])
            else:
                return max(LCS_recursion(X[i+1:],Y[j:]), LCS_recursion(X[i:], Y[j+1:]))
# %%
X = "AGGTAB"
Y = "GXTXAYB"

LCS_recursion(X,Y)
# %%
# Longest Common Subsequence - by memoization
def LCS_memoization(X,Y,T):
    if len(X) == 0 or len(Y) == 0:
        return 0
    for i in range(len(X)):
        for j in range(len(Y)):
            if X[i] == Y[j]:
                T[i][j] = 1 + LCS_memoization(X[i+1:], Y[j+1:], T)
            else:
                T[i][j] = max(LCS_memoization(X[i+1:],Y[j:],T), LCS_memoization(X[i:], Y[j+1:],T))
            return T[i][j]
# %%
X = "AGGTAB"
Y = "GXTXAYB"

rows = len(X)
cols = len(Y)

T = [[0 for i in range(cols)] for j in range(rows)]

LCS_memoization(X,Y,T)
# %%
#Longest common subsequence - Dynamic Programming


def LCS_Dynamic(X, Y):
    X =  " " + X  # add additional space for padding
    Y =  " " + Y
    rows = len(X)
    cols = len(Y)
    T = [[0 for i in range(cols)] for j in range(rows)]
    maxlen = 0
    for i in range(1, rows):
        for j in range(1, cols):
            if X[i] == Y[j]:
                T[i][j] = 1 + T[i-1][j-1]
            else:
                T[i][j] = max(T[i-1][j], T[i][j-1])
    maxlen = T[rows-1][cols-1]
    substr = ""
    for i in range(1,rows):
        for j in range(1,cols):
            if T[i][j] > T[i-1][j] and T[i][j] > T[i][j-1] \
                        and T[i][j] == T[i-1][j-1]+1:
                substr += X[i]
    print(maxlen, substr)
    for v in T:
        print(v)

# %%
X = "abcdef"
Y = "pqrbrceuf"

LCS_Dynamic(X,Y)


# %%
# Longest Palindromic subsequence

X = "aaaabbaa"
Y = X[::-1]

LCS_Palindromic_Dynamic(X,Y)

# %%
#Longest palindromic subsequence - Dynamic Programming
#Using longest common subsequence method


def LCS_Palindromic_Dynamic(X, Y):
    X =  " " + X  # add additional space for padding
    Y =  " " + Y
    rows = len(X)
    cols = len(Y)
    T = [[0 for i in range(cols)] for j in range(rows)]
    maxlen = 0
    for i in range(1, rows):
        for j in range(1, cols):
            if X[i] == Y[j]:
                T[i][j] = 1 + T[i-1][j-1]
            else:
                T[i][j] = max(T[i-1][j], T[i][j-1])
    maxlen = T[rows-1][cols-1]
    substr = ""
    for i in range(1,rows):
            if T[i][] == T[i-1][j-1]+1:
                substr += X[i]
    print(maxlen, substr)
    for v in T:
        print(v)