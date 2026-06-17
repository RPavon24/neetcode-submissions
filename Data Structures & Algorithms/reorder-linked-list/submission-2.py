# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head

        while fast: 
            fast = fast.next.next if fast.next else None
            if not fast: 
                nextNode = slow.next
                slow.next = None
                slow = nextNode
            else: 
                slow = slow.next

            
        prev = None
        curr = slow
        while curr: 
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        l1 = head
        l2 = prev

        # while l1: 
        #     print(l1.val)
        #     l1 = l1.next
        # print("\n--------\n")
        # while l2: 
        #     print(l2.val)
        #     l2 = l2.next

        while l2 or l1:
            l1_next = l1.next if l1 else None
            l2_next = l2.next if l2 else None


            l1.next = l2
            if not l2: 
                break
            l2.next = l1_next
            l1 = l1_next
            l2 = l2_next

            

