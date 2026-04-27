class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i] = 1
        freqList = []
        for key, value in dic.items():
            freqList.append((value, key))
        freqList.sort()
        result = []
        for i in range(len(freqList)-1, len(freqList) - k - 1, -1):
            result.append(freqList[i][1])
        return result