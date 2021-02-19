class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Leetcode 3 - Longest substring without repeating characters
        st = en = poi = 0

        substr = temp = ''
        maxlen = 0
        for i in range(len(s)):
            if s[i] not in temp:
                temp += s[i]
            else:
                if maxlen < len(temp):
                    maxlen = len(temp)
                    substr = temp
                    st = poi
                    en = i - 1
                while s[i] in temp:
                    temp = temp[1:]
                    poi = poi + i
                temp += s[i]
        if maxlen < len(temp):
            maxlen = len(temp)
            substr = temp
        #print(f"Longest substring is {substr} and length is {maxlen} and from {st} to {en}")
        return(maxlen)