class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictionary = {}
        for letter in s:
            if letter in dictionary:
                dictionary[letter]+=1
            else:
                dictionary[letter]=1
        for letter in t:
            if letter in dictionary:
                dictionary[letter]-=1
            else:
                return False
        return all(value == 0 for value in dictionary.values())