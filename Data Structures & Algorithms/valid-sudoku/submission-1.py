class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9): 
            if not self.isRowValid(board[i]): 
                return False
        Rows_valid = True


        for j in range(9): 
            col = []
            for i in range(9): 
                col.append(board[i][j])
            if not self.isColValid(col): 
                return False
        ColsValid = True

        
        for i in [2,5,8]:
            for j in [2,5,8]: 
                if not self.isSquareValid(board, i, j): 
                    return False
        
        return True


    def isRowValid(self, row: List[str]) -> bool:
        nums = set()
        for s in row: 
            if s == ".": 
                continue
            n = int(s)
            if s not in nums: 
                nums.add(s)
            else: 
                return False
        return True


    def isColValid(self, col : List[str]) -> bool: 
        nums = set()
        for s in col: 
            if s == ".": 
                continue
            n = int(s)
            if s not in nums: 
                nums.add(s)
            else: 
                return False
        return True

    def isSquareValid(self, board: List[List[str]], i: int, j: int) -> bool:
        nums = set()
        idx_i = i
        for _ in range(3): 
            idx_j = j
            for _ in range(3): 
                if board[idx_i][idx_j] == ".": 
                    idx_j -= 1
                    continue
                n = int(board[idx_i][idx_j])
                if n not in nums: 
                    nums.add(n)
                else: 
                    return False
                idx_j -= 1
            idx_i -= 1
        return True
