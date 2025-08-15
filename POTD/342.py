def isPowerOfFour(self, n: int) -> bool:
        '''
        # With Loop
        
        for i in range(16):
            if n == 4**i:
                return True
        
        return False
        '''

        # Without Loop

        return n > 0 and 1073741824 % n == 0 and int(n**0.5)**2 == n
    
'''
# Java Code

class Solution {
    public boolean isPowerOfFour(int n) {
        /*
        for(int i = 0; i<16; i++){
            if(n == Math.pow(4,i)){
                return true;
            }
        }
        return false; 
    */

    return n > 0 && (n & (n - 1)) == 0 && (n & 0x55555555) != 0;
    }
}

'''