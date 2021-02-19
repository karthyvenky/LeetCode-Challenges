#%%
A = [12,24,8,32]
B = [13,25,32,11]
A = [2,7,11,15]
B = [1,10,4,11]

ans = [0] * len(A)
index = sorted(range(len(B)), key=lambda x:B[x], reverse=True)
remaining = []
for a in sorted(A):
    if a > B[index[-1]]:
        ans[index.pop()] = a
    else:
        remaining.append(a)
for b, a in zip(index, remaining):
    ans[b] = a
return ans
        





#%%

A = [12,24,8,32]
# print(sorted(range(len(A)),key= lambda x:A[x],reverse=True))
A.pop()
A
A.pop()
A
# %%
A = [12,24,8,32]
B = [13,25,32,11]
A = [2,7,11,15]
B = [7,10,4,11]
#A = [2,7,11,15]
#B = [1,4,10,11]
result = [-1]*len(A)
blist = []
#to store the original position
blist = sorted([(b,i) for i, b in enumerate(B)])
#now sort both the arrays
blist = collections.deque((blist))

for a in sorted(A):
    if a >  blist[0][0]:
        val, idx = blist.popleft()
    else:
        val, idx = blist.pop()
    
    result[idx] = a
return result


# %%
