class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        boundaries = [(0,0) for _ in range(len(heights))]

        left=[]
        for i in range(len(heights)):
            while left and heights[left[-1]] > heights[i]: 
                left.pop()
            l = left[-1] if left else -1
            left.append(i)
            boundaries[i] = (l , 0)
        right = []
        for i in range(len(heights) - 1, -1, -1):
            while right and heights[right[-1]] >= heights[i]: 
                right.pop()
            r = right[-1] if right else len(heights)
            right.append(i)
            l, _ = boundaries[i]
            boundaries[i] = (l, r)
        curr = 0
        for i in range(len(heights)):
            l,r = boundaries[i]
            width = r - l - 1
            print(heights[i], width)
            curr = max(curr, (heights[i] * width))
        print(boundaries)
        return curr
        

            



