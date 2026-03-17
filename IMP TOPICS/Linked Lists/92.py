# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        #1: Reach node at position left

        dummy = ListNode(0, head)
        leftPrev = dummy
        curr = head

        for i in range(left-1):
            leftPrev = curr
            curr = curr.next


        # 2: Reverse
        prev = None
        for i in range(right- left + 1):
            tempNext = curr.next
            curr.next = prev
            prev = curr
            curr = tempNext

        # 3: Update Pointers

        leftPrev.next.next = curr
        leftPrev.next = prev

        return dummy.next