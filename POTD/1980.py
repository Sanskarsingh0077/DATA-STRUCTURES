class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        '''
        k = len(nums)
        l = []
        for i in range(2**k):
            binary = bin(i)[2:].zfill(k)
            l.append(binary)
        
        l.sort()
        nums.sort()

        for i in range(len(nums)):
            if nums[i] != l[i]:
                return l[i]

        return l[-1]   

        '''

        res = []

        for i in range(len(nums)):
            if nums[i][i] == '0':
                res.append('1')

            else:
                res.append('0')

        return ''.join(res)

             

