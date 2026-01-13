# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_ll(arr):
    dummy = ListNode()
    cur = dummy
    for x in arr:
        cur.next = ListNode(x)
        cur = cur.next
    return dummy.next

def print_ll(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    print(res)
    
class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)

        def mergetwo(l1, l2): # O(N)
            dummy = ListNode()

            if l1 is None:
                return l2

            if l2 is None:
                return l1

            if l1.val < l2.val:
                dummy = l1
                dummy.next = mergetwo(l1.next, l2)

            else:
                dummy = l2
                dummy.next = mergetwo(l1, l2.next)

            return dummy

        def divideAndConq(left,right): # O(log K)
            if left == right:
                return lists[left]

            mid = left + (right - left)// 2

            l1 = divideAndConq(left, mid)
            l2 = divideAndConq(mid+1, right)

            return mergetwo(l1,l2)

        if not lists:
            return None

        return divideAndConq(0, n-1)


        '''
        Time Complexity: O( N log K )

        N : total number of nodes across all lists
        Log K : Number of levels in binary search Tree


        '''

lists = [build_ll([1,4,5]), build_ll([1,3,4]), build_ll([2,6])]
sol = Solution()
ans = sol.mergeKLists(lists)
print_ll(ans)
