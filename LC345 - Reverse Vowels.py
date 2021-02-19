string = "leetcode"

def reversevowels(string):
    string = list(string)
    t = []
    t[:] = string
    _d = [i for i,c in enumerate(string) if c in "AEIOUaeiou"]
    for i,j in zip(_d,_d[::-1]):
        string[i] = t[j]
    string = "".join(string)
    return(string)

print(reversevowels(string))