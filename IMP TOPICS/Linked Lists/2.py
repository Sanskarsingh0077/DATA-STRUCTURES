# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0) # new list
        curr = res #pointing to new list
        carry = 0

        while l1 or l2 or carry: 
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry # Calculate total
            carry = total // 10 # Calculate carry

            curr.next = ListNode(total % 10) # make new node
            curr = curr.next # Move Pointer

            if l1:
                l1 = l1.next # move next

            if l2:
                l2 = l2.next

        return res.next