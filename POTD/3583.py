class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        n = len(nums)

        # One Pass Solution

        valid_i = defaultdict(int)
        valid_j = defaultdict(int)

        res = 0

        for num in nums:
            if num % 2 == 0:
                res = (res + valid_j[num/2]) % mod

            valid_j[num] = (valid_j[num] + valid_i[num*2]) % mod

            valid_i[num] += 1

        return res

        # Two Pass Approach (O(n + n)) 
'''
        res = 0

        left_mp = defaultdict(int)
        right_mp = defaultdict(int)

        for x in nums:
            right_mp[x] += 1

        for num in nums:
            right_mp[num] -= 1


            right = right_mp[num*2]
            left = left_mp[num*2]

            res = (res + (left * right)) % mod

            left_mp[num] += 1

        return res
'''

        
 
 




