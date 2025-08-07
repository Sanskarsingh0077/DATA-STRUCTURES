class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        '''
        #String Approach:
        new=int(str(abs(x))[::-1])
        result = sign * new
        

        if -2**31 <= result <= 2**31 - 1:
            return result
            
        else:
            return 0

        '''
        #Mathematical approach:
        result= 0
        x=abs(x)
        while x!=0:
            digit = x% 10
            result = result *10 + digit
            x //= 10

        ans= sign* result

        if -2**31 <= ans <= 2**31 - 1:
            return ans

        else:
            return 0


        
        '''
         Total Time Complexity: O(d), where d is the number of digits in x (at most 10 for 32-bit integers)
         Total Space Complexity: O(d)
        '''