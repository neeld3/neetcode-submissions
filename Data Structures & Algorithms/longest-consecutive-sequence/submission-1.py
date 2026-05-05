class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        available = set()
        for i in nums:
            available.add(i)
        
        maxSequence = 0
        for i in nums:
            currSequence = 0
            curr = i
            while curr in available:
                currSequence += 1
                curr += 1
            maxSequence = max(maxSequence, currSequence)
        return maxSequence