class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for i in range(len(nums)):
            dictionary[nums[i]] = i
        for i in range(len(nums)):
            val = target - nums[i]
            if val in dictionary and dictionary[val] != i:
                return [i, dictionary[val]]