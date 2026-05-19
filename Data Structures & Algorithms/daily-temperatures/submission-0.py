class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0 for _ in range(len(temperatures))]
        for i in range(len(temperatures)): 
            for j in range(i + 1, len(temperatures)): 
                if temperatures[i] < temperatures[j]: 
                    results[i] = j - i
                    break
        return results