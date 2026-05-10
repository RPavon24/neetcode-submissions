import sys
class MinStack:
    def __init__(self):
        self.stack = []
        self.least = sys.maxsize
    
    def push(self, val: int) -> None:
        self.stack.append((val, self.least))
        if self.least > val: 
            self.least = val
        

    def pop(self) -> None:
        prev = self.stack.pop()
        self.least = prev[1]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.least
        
