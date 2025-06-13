class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]*(n+1)

        '''
        
        # O(nlogn) Approach:

        for i in range(1,n+1):
                ans[i]=(bin(i).count('1'))

        return ans
        '''

        # O(n) Approach:
        '''

        for i in range(1,n+1):
            if i%2 != 0:
                ans[i] = ans[i//2] +1

            else:
                ans[i] = ans[i//2]

        return ans
        '''
        # Another approach
        for i in range(1,n+1):
            ans[i] = ans[i & (i-1)] +1 #using & operator
        return ans
