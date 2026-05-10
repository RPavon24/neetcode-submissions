class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # mynums = [(num, i) for i, num in enumerate(nums)]
        mynums = sorted(nums)
        solution = []
        solutionset = set()
        for i, num in enumerate(mynums): 
            p1 = 0
            p2 = len(mynums) - 1
            target = num * -1
            while p1 < p2: 
                if p1 == i: 
                    p1 += 1
                    continue
                if p2 == i: 
                    p2 -=1 
                    continue
                cursum = mynums[p1] + mynums[p2]
                # print(num, target, cursum)
                if cursum == target:
                    if tuple(sorted([num, mynums[p1], mynums[p2]])) not in solutionset: 
                        # print(num, mynums[p1], mynums[p2])
                        # print(i, p1, p2)
                        solutionset.add(tuple(sorted([num, mynums[p1], mynums[p2]])))
                        solution.append([num, mynums[p1], mynums[p2]])
                    p1+=1
                    p2 -=1
                elif cursum > target : 
                    p2 -= 1
                else: 
                    p1 += 1
        return list(solution)





