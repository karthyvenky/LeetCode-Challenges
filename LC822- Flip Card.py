fronts = [1,2,4,4,7]
backs = [1,3,4,1,3]

def flipgame(fronts, backs):
 
	poison_numbers = set(f for f,b in zip(fronts, backs) if f == b)
	choices = set(fronts + backs) - poison_numbers
	return min(choices) if choices else 0
    
print(flipgame(fronts,backs))