# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Function to get Kth Node in each group
    def get_kth(self, temp, k): 
        k -= 1
        while temp and k > 0:
            k -= 1
            temp = temp.next

        return temp

    # Function to reverse the k sized Linked List
    def reverse_LL(self, node): 
        if node is None or node.next is None:
                return node

        last = self.reverse_LL(node.next)
        node.next.next = node
        node.next = None

        return last



    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        temp = head
        prevNode = None

        while temp:
            kth = self.get_kth(temp, k) # get Kth

            # If remaining nodes are less than k, attach as-is
            if not kth: 
                if prevNode:
                    prevNode.next = temp
                    break

            # Seperate Linked List Group with full LL
            nextnode = kth.next # node after k-group (Preserve Start of next List)
            kth.next   = None   # detach kth Node from LL (Detach Current List for Reverse)

            new_head = self.reverse_LL(temp) # Reverse K sized LL

            # Update head if first group
            if temp == head:
                head = new_head
            
            else:
                prevNode.next = new_head
            
            # temp is now tail after reversal
            prevNode = temp
            temp = nextnode

        return head


        
    
    
