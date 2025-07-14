# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        '''
        def bin_to_dec(binary_str:str): # Function for converting binary to decimal
            result = 0

            for digit in binary_str:
                result = result * 2 + int(digit)

            return result

        binary_str = ""

        while head: # access each value
            binary_str += str(head.val)
            head = head.next

        return bin_to_dec(binary_str)
        '''

        #Optimized Space solution

        result = 0

        while head:
            result = result * 2 + head.val
            head = head.next

        return result

        # TC : O(n)
        # SC : O(1)