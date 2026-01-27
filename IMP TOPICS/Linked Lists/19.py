class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0 , head)
        left = dummy
        right = head

        # Move right n ahead
        while right and n > 0:
            right = right.next
            n -= 1

        # Move left right Pointers
        while right:
            left = left.next
            right = right.next
            
        # Delete Node by repointing

        left.next = left.next.next

        return dummy.next # Return the next from head
    
    #TC : Used Two Pointers O(n)
    #SC : O(1) -- Created only dummy Node(0)