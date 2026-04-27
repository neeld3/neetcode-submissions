class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictionary = {}
        if len(s) != len(t):
            return False
        for i in s:
            if i not in dictionary:
                dictionary[i] = 1
            else:
                dictionary[i] += 1
        for j in t:
            if j in dictionary and dictionary[j]>0:
                dictionary[j]-=1
            else:
                return False
        return True