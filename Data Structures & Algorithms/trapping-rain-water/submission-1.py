class Solution:
    def trap(self, height: List[int]) -> int: 
        n = len(height)
        prefix = [0 for _ in range(n)]
        suffix = [0 for _ in range(n)]
        #suffix
        mx = height[n - 1]
        for i in range(n - 1, -1, -1): 
            if height[i] > mx: 
                mx = height[i]
            suffix[i] = mx
        mx = height[0]
        for i in range(n):
            if height[i] > mx : 
                mx = height[i]
            prefix[i] = mx

        total = 0
        answer = []
        for i, h in enumerate(height): 
            l = prefix[i]
            r = suffix[i]
            value = min(l, r) - h #if min(l,r) - h >= 0 else 0
            total += value
            answer.append(value)
        
        print(answer)

        return total
