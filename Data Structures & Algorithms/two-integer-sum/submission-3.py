class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val = {}
        for i in range(len(nums)):
            val[nums[i]] = i
        
        for i in range(len(nums)):
            j = target - nums[i]
            if j in val and val[j] != i:
                return [i, val[j]]