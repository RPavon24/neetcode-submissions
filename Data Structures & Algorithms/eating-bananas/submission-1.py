class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:        
        def works (k :  int): 
            count = 0
            for pile in piles: 
                count += math.ceil(pile / k)
            if count <= h: 
                return 1
            else: #count > h  = k was too small
                return -1
        #from 1 to max(piles)
        start = 1
        stop = max(piles)
        sol = max(piles)
        while start != stop: 
            midpoint = (start + stop) // 2
            result = works(midpoint)
            if  result == 1: 
                sol = midpoint
                stop = midpoint 
            else: 
                start = midpoint + 1
        return stop


