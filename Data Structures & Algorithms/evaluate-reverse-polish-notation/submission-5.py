class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #mathematical notation in which operators follow their operands
        stack = []
        o1 = int
        o2 = int
        for tok in tokens: 
            if tok in "+-/*": 
                op = tok
            else: 
                stack.append(int(tok))
                continue
            o2 = stack.pop()
            o1 = stack.pop()
            print(o1, o2, op)
            if op == "+": 
                stack.append(o1 + o2)
            elif op == "-": 
                stack.append(o1 - o2)
            elif op == "*": 
                stack.append(o1 * o2)
            elif op == "/":
                stack.append(int(o1 / o2))    
        return stack[0]

            
