# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Edge case: If the list has only one node, return None (empty list)
        if not head or not head.next:
            return None

        curr = head
        count= 0 

        # Step 1: Traverse to find the length of the linked list
        while curr:
            count+=1
            curr=curr.next

        mid_node = count // 2 # Step 2: Find the middle node (index will be count // 2)

        curr = head

        # Step 3: Traverse again to reach the node just before the middle node
        for _ in range(mid_node-1):
            curr = curr.next

        curr.next = curr.next.next # Step 4: Skip the middle node by modifying the next pointer

        return head


        '''
        Approach:
	1.	Traverse the List to Find the Length: First, traverse the linked list to count the total number of nodes.
	2.	Find the Middle Node: The middle node can be located at count // 2 index.
	3.	Traverse Again to the Node Before the Middle: Traverse again to find the node just before the middle node.
	4.	Delete the Middle Node: Change the next pointer of the node before the middle node to skip the middle node.


        '''


        

        