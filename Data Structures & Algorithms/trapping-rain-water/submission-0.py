class Solution:
    def trap(self, height: List[int]) -> int: 
        precompute = []
        n = len(height)
        for i , h in enumerate(height): 
            prefix = max(height[:i]) if len(height[:i]) > 0 else 0
            suffix = max(height[i:]) if len(height[i:]) > 0 else 0
            precompute.append((prefix, suffix))

        total = 0
        answer = []
        for i, h in enumerate(height): 
            l, r = precompute[i]
            value = min(l, r) - h if min(l,r) - h >= 0 else 0
            total += value
            answer.append(value)
        
        print(answer)

        return total
