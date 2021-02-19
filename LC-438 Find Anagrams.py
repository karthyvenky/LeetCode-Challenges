from collections import Counter, defaultdict

def minWindow(s, t):
	if len(s) < len(t):
		return ""
	scount = Counter()
	tcount = Counter(t)
	l  = 0
	cnt = len(t)
	minstring = s
	minlen = len(s)
	
	for r ,c in enumerate(s):
		if c in tcount:
			scount[c] += 1
			if scount[c] <= tcount[c]:
				cnt -= 1
			if cnt == 0:
				while s[l] not in tcount or scount[s[l]] != tcount[s[l]]:
					if s[l] in tcount and scount[s[l]] > tcount[s[l]]:
						scount[s[l]] -= 1
					l += 1
				if minlen > r - l + 1:
					minlen  = r - l + 1
					minstring = s[l:r+1]
	if cnt !=0:
		return ""
	return minstring

def findanagrams(s,t):
	if len(s) < len(t):
		return[]
	tcount = Counter(t)
	scount = Counter()
	l = 0
	cnt = len(t)
	poi = []
	
	for r, c in enumerate(s):
		if c in tcount:
			scount[c] += 1
			if scount[c] <= tcount[c]:
				cnt -= 1
			if cnt == 0:
				while s[l] not in tcount or scount[s[l]] != tcount[s[l]]:
					if s[l] in tcount and scount[s[l]] > tcount[s[l]]:
						scount[s[l]] -= 1
					l += 1
				if len(t) == r - l + 1:
					poi.append(l)
	if cnt !=0:
		return []
	return poi
	



s = "abab"
t = "ab"
print(findanagrams(s,t))
				
				
	
	
	
	




