class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def recurse(start, stop) -> int: 
            print(nums[start:stop], start, stop)
            if start == stop: 
                return -1
            idx = (stop + start) // 2
            curr = nums[idx]
            if curr == target : 
                return idx
            elif curr > target: # left
                print('left')
                return recurse(start, idx)
            elif curr  < target:  # right
                print('right')
                return recurse(idx + 1, stop)

        
        return recurse(0, len(nums))