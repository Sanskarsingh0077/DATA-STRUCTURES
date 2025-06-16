class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        # Right Most bit Exploration :- num & 1
        # Right Shift :- num >>= 1

        flips = 0

        #This loop continues as long as at least one of the numbers (a, b, or c) still has bits left to process.
        while a != 0 or b != 0 or c != 0:  
            abit = a & 1
            bbit = b & 1
            cbit = c & 1

            if abit | bbit != cbit:
                if cbit == 0:
                    flips += abit + bbit
                
                else:                           # cbit == 1 but both abit and bbit are 0
                    if abit == 0 or bbit == 0:  # At least one must be 1 → flip one if both are 0
                        flips += 1
            

            a >>= 1
            b >>= 1
            c >>= 1
      
        return flips

