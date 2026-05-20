class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0 for _ in range(len(temperatures))]
        stack = []
        for i, temp in enumerate(temperatures): 
            if not stack: 
                stack.append((i, temp))
                continue

            while stack and stack[-1][1] < temp: 
                j, _ = stack.pop()
                results[j] = i - j; 
            stack.append((i, temp))
        
        return results