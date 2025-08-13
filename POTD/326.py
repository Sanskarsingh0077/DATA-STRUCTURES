def isPowerOfThree(self, n: int) -> bool:
        '''

        for i in range(31):
            if n == 3**i:
                return True

        return False

        Time Complexity: O(n)

        '''

        return n>0 and 3**19 % n == 0 #(1162261467 is 3^19, the largest power of 3 that fits in a 32-bit signed int)

        #Time Complexity: O(1)
        
        #Java Code
        '''
        class Solution {
    public boolean isPowerOfThree(int n) {
        return n>0 && 1162261467 % n == 0;

    }
    }
        
        
        '''