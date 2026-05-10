# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        temp = None; 

        while list1 is not None and list2 is not None:
            if head.next is None: 
                if list1.val > list2.val: 
                    head.next = list2
                    temp = list2
                    list2 = list2.next
                    continue
                else: 
                    head.next = list1
                    temp = list1
                    list1 = list1.next
                    continue

            if list1.val > list2.val: 
                temp.next = list2
                temp = list2
                list2 = list2.next
            else:
                temp.next = list1
                temp = list1
                list1 = list1.next

        if head.next is None: 
            if list1 is not None: 
                return list1
            elif list2 is not None:
                return list2
        
        if list1 is not None and list2 is None: 
            temp.next = list1
        elif list2 is not None and list1 is None: 
            temp.next = list2
        return head.next

