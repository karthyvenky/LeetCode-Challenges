#%%

n = 8
T = [0 for i in range(n+1)]
T[0] = 1
T[1] = 1

for i in range(2,n+1):
    T[i] = T[i-1] + T[i-2]
print(T[n])
print(T)
# %%
class Solution:
    def climbStairs(self, n: int) -> int:
        T = [0 for i in range(n+1)]
        T[0] = 1
        T[1] = 1

        for i in range(2,n+1):
            T[i] = T[i-1] + T[i-2]
        return(T[n])
