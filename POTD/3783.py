class Solution:
    def mirrorDistance(self, n: int) -> int:
        def reverse(x):
            rev = 0
            while x:
                rev = rev * 10 + x % 10
                x //= 10
            return rev
            
        return abs(n - reverse(n))
