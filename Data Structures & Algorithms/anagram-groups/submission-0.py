class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        for i in strs:
            word = "".join(sorted(i)) 
            if word in dictionary:
                dictionary[word].append(i)
            else:
                dictionary[word] = [i]
        result = []
        for value in dictionary.values():
            result.append(value)
        return result