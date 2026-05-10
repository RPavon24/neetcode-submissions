class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def calcArea(l, r): 
            h = min(heights[l], heights[r])
            w = r - l
            return w * h

        l = 0
        r = len(heights) -1
        maxArea = 0 
        while l < r: 
            area = calcArea(l,r)
            if area > maxArea: 
                maxArea = area
            if heights[l] > heights[r]: 
                r -= 1
            elif heights[r] > heights[l]: 
                l += 1
            else: 
                l += 1
                r -= 1
        return maxArea