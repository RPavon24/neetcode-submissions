class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set()
        longest = 0

        for i in nums: 
            numSet.add(i)

        for i in numSet:
            if(i - 1) in numSet:
                continue
            current = i
            length = 1
            while((current + 1) in numSet): 
                length = length + 1
                current = current + 1
            if(longest < length):
                longest = length; 

        return longest    