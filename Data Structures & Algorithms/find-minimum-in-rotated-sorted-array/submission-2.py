class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[-1] > nums[0]: 
            return nums[0]

        l = 0
        r = len(nums) - 1
        while l <= r: 
            mid = (l + r ) // 2

            if nums[l] <= nums[mid] and nums[mid] > nums[r]: #min cannot be in this half
                l = mid + 1
            elif nums[mid] < nums[r]: #min could be in mid
                r = mid
            else : 
                return nums[mid]

