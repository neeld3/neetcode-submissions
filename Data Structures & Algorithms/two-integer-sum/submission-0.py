class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        items = {}
        for i, n in enumerate(nums):
            items[n] = i
        
        for i, n in enumerate(nums):
            res = target - n
            if res in items and items[res] != i:
                return [i, items[res]]
