#%%
nums = [3,4,5,2]
max1 = max2 = -1<<31
for v in nums:
    if max1 < v:
        max2 = max1
        max1 = v
    elif max2 < v:
        max2 = v
print((max1-1) * (max2-1))
    
    

# %%
