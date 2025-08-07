class Solution:
    def isPalindrome(self, x: int) -> bool:
        '''
        #String Reverse:
        
        if x == int(str(abs(x))[::-1]):
            return True
        else:
            return False
        
        '''
        #Mathematical Reverse:
        original = x
        result = 0

        if x<0:
            return False

        while x!=0:
            digit = x % 10
            result = result * 10 + digit
            x //= 10

        return original == result
        

        

