#%%
#Zigzag conversion

s = "PAYPALISHIRING"
numRows = 3

if numRows == 0 or numRows == 1:
    print(s)

ls = ['']*numRows
row = 0
goingup = False
 
for c in s:
    ls[row] += c
    if row >= numRows -1 :
        goingup = True
    elif row <= 0:
        goingup = False
    
    if goingup:
        row -= 1
    else:
        row += 1
    
print("".join(ls))
        

        

# %%

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 0 or numRows == 1:
            return(s)

        ls = ['']*numRows
        row = 0
        goingup = False

        for c in s:
            ls[row] += c
            if row >= numRows -1 :
                goingup = True
            elif row <= 0:
                goingup = False

            if goingup:
                row -= 1
            else:
                row += 1

        return("".join(ls))
# %%
convert("PAYPALISHIRING",4)
# %%

def reverse(num: int) -> int:
    rnum = 0
    sign = False
    if (-1 << 31) <= num <= (1 << 31)+1:
        if num < 0:
            sign = True
            num = num * -1
        while num:
            num,digit = divmod(num,10)
            rnum = rnum*10 + digit

        if sign:
            rnum = rnum * - 1
        if (-1 << 31) <= rnum <= (1 << 31)+1:
            return(rnum)
        else:
            return(0)
    else:
        return(0)
    
    
# %%
print(reverse(1<<32 ))
# %%
