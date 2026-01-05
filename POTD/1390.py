class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        # Brute Force O(n * max(nums)) - TLE
        '''
        total = 0

        for num in nums:
            res = []
            for value in range(1, num+1):
                if num % value == 0:
                    res.append(value)

            if len(res) == 4:
                total += sum(res)

        return total

        '''

        # Optimization - O(n * max(nums)**0.5)


        total = 0

        for num in nums: # O(n)
            div_sum = 0
            count = 0

            for p in range(1, int(num**0.5)+1): # O(max(nums)**0.5)
                if num % p == 0:
                    q = num // p

                    if q != p:
                        count += 2
                        div_sum += p + q

                    else:
                        count += 1
                        div_sum += p

                if count > 4:
                    break

            if count == 4:
                total += div_sum

        return total



