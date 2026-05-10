class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s: 
            if char in ['(', '{', '[']: 
                stack.append(char)
            elif char in [')', '}', ']']:
                if len(stack) == 0:
                    return False
                if self.isPair(stack[-1], char):
                    stack.pop() 
                else:
                    return False
        return len(stack) == 0

    def isPair(self, c1: str, c2:str):
        if c1 == '(' and c2 == ')': 
            return True
        elif c1 == '[' and c2 ==']':
            return True
        elif c1 == '{' and c2 == '}': 
            return True
        else:
            return False
