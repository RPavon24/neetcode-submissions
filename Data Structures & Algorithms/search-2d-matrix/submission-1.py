class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix)
        n = len(matrix[0])
        row = self.binarySearchMatrix(matrix, m, 0, target)
        if row == -1: 
            return False
        else :
            return self.binarySearchRow(matrix[row], n, 0, target)

        
    def binarySearchMatrix(self, matrix: List[List[int]], upper: int, lower: int, target: int) -> int:
        if upper < lower:
            return -1
        mid = (upper + lower) // 2
        if mid >= len(matrix): 
            return -1
            
        if matrix[mid][0] > target: 
            return self.binarySearchMatrix(matrix, mid -1, lower, target)
        elif matrix[mid][len(matrix[0]) - 1] < target: 
            return self.binarySearchMatrix(matrix, upper, mid + 1, target)
        else: 
            return mid

    def binarySearchRow(self, row: List[int], upper: int, lower: int, target: int) -> bool:
        if upper < lower: 
            return False

        mid = (upper + lower) // 2

        if row[mid] > target: 
            return self.binarySearchRow(row, mid -1, lower, target)
        elif row[mid] < target: 
            return self.binarySearchRow(row, upper, mid +1, target)
        else: 
            return True