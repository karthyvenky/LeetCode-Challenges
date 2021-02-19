#%%
def sortballs(low, high):
    boxes = {}
    for i in range(low,high+1):
        #s = str(i)
        tot = 0
        while i:
            i,d = divmod(i,10)
            tot += int(d)
        boxes[tot] = boxes.get(tot,0) + 1
    return(max(boxes.values()))
    # return(max(boxes,key=boxes.get))
    
        
           
   
    
# %%
# print(sortballs(1,10))
print(sortballs(1,10))


# %%
class Solution: #Faster solution
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        boxes = {}
        for i in range(lowLimit,highLimit+1):
            tot = sum(map(int,str(i)))
            boxes[tot] = boxes.get(tot,0) + 1
        return(max(boxes.values()))
# %%

num = 123
sum(map(int,str(num)))