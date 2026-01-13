# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #Recursive Method
        '''
        dummy = ListNode()
        if l1 is None:
            return l2

        if l2 is None:
            return l1

        if l1.val < l2.val:
            dummy = l1
            dummy.next = self.mergeTwoLists(l1.next,l2)

        else:
            dummy = l2
            dummy.next = self.mergeTwoLists(l1, l2.next)

        return dummy

        '''

        # Iterative

        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next

            else:
                tail.next = l2
                l2 = l2.next

            tail = tail.next

        if l1:
            tail.next = l1

        else:
            tail.next = l2

        return dummy.next
