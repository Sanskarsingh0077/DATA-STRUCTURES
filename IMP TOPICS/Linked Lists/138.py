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
        mp = {None : None}

        #Create Nodes and store in map
        curr = head
        while curr:
            copy = Node(curr.val)
            mp[curr] = copy
            curr = curr.next

        #Link Nodes and store Values
        curr = head
        while curr:
            copy = mp[curr]
            copy.next = mp[curr.next]
            copy.random = mp[curr.random]
            curr = curr.next

        return mp[head] # copy Node

        #TC : O(n) ---> One Pass each
        #SC : O(n) ---> Hash Map with n Nodes

        

