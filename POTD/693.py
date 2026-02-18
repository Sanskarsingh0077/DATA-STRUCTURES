class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        '''
        highestsetbit = n.bit_length()-1
        b = f"{n:032b}"

        start = 32 - (highestsetbit + 1)

        for i in range(start, 31):
            if b[i] == b[i+1]:
                return False

        return True

        '''
        '''
        currbit = n % 2
        n = n // 2

        while n > 0:
            nextbit = n % 2
            if currbit == nextbit:
                return False

            currbit = nextbit
            n = n // 2

        return True

        '''

        #Bit Right Shift

        x = (n ^ (n>>1))
        
        return (x & (x+1)) == 0


