"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: 
            return None
        dic = {}
        tmp = head
        prev = Node(head.val)
        dic[head] = prev
        newHead = prev
        while tmp and tmp.next: 
            prev.next = Node(tmp.next.val)
            prev = prev.next
            dic[tmp.next] = prev
            tmp = tmp.next
        
        tmp = newHead
        tmp2 = head
        while tmp: 
            tmp.random = dic[tmp2.random] if tmp2.random else None
            tmp = tmp.next
            tmp2 = tmp2.next

        # - printing - 
        # tmp = newHead
        # while tmp: 
        #     print(tmp.val)
        #     tmp = tmp.next
        

        return newHead

        