class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = -1
        l = 0
        r = len(heights)-1
        while l<r:
            minHeight  = min(heights[r], heights[l])
            length = r-l
            currArea = minHeight*length
            maxArea = max(maxArea, currArea)
            if heights[l] <= heights[r]:
                l+=1
            else:
                r-=1
        return maxArea