class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        #depth first search on every one we find that is new? 

        found = set()
        maxIsland = 0

        for m in range(len(grid)): 
            for n in range(len(grid[m])): 
                if((grid[m][n] == 1) and ((m,n) not in found)): 
                    maxIsland = max(maxIsland, self.DFSCount(found, m, n, grid) )

        return maxIsland
                


    def DFSCount(self, found: set, m: int, n: int, grid: List[List[int]]) -> int:
        stack = []
        count = 0
        stack.append((m,n))
        while len(stack) != 0:
            current = stack.pop() 
            if(current in found):
                    continue
            found.add(current)  
            i = current[0]
            j = current[1]
            if j - 1 > 0:
                if grid[i][j -1] == 1 and (i, j-1) not in found:
                    stack.append((i, j -1))
            if j + 1 < len(grid[i]):
                if grid[i][j + 1] == 1 and (i, j+1) not in found: 
                    stack.append((i, j + 1))
            if i + 1 < len(grid):
                if grid[i+1][j] == 1 and (i +1, j) not in found: 
                    stack.append((i + 1, j)) 
            if i - 1 > 0: 
                if grid[i-1][j] == 1 and (i-1, j) not in found: 
                    stack.append((i-1, j))
            count = count +1

        return count

