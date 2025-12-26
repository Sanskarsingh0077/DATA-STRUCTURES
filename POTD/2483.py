class Solution:
    def bestClosingTime(self, customers: str) -> int:
        # Brute Force(O(N * N))
        '''

        n = len(customers)

        minPenalty = float('inf')
        minHour = float('inf')

        for i in range(n):

            # Left Opened Part
            j = i -1
            penalty = 0

            while j >= 0:
                if customers[j] == 'N':
                    penalty += 1
                j -= 1
            # Right closed Part
            j = i

            while j < n:
                if customers[j] == 'Y':
                    penalty += 1

                j += 1

            if penalty < minPenalty:
                minPenalty = penalty

                minHour = i

        # Closing at nth hour
        # 0 - n-1 --> 'N' penalty++

        nthHourPenalty = customers.count('N')
        if nthHourPenalty < minPenalty:
            minHour = n

        return minHour

        '''

        # Optimized Approach (Prefix Sum And Suffix Sum)

        '''

        n = len(customers)
        prefix_N = [0]*(n+1)
        suffix_Y = [0]*(n+1)

        prefix_N[0] = 0
        suffix_Y[n] = 0

        for i in range(1, n+1):
            if customers[i-1] == 'N':
                prefix_N[i] = prefix_N[i-1] + 1

            else:
                prefix_N[i] = prefix_N[i-1]


        for i in range(n-1,-1,-1):
            if customers[i] == 'Y':
                suffix_Y[i] = suffix_Y[i+1] + 1

            else:
                suffix_Y[i] = suffix_Y[i+1]

        minPenalty = float('inf')
        minHour = float('inf')

        for i in range(n+1):
            currPenalty = prefix_N[i] + suffix_Y[i]

            if currPenalty < minPenalty:
                minPenalty = currPenalty
                minHour = i

        return minHour
        '''

        # Optimized O(1) Space Solution

        n = len(customers)

        minHour = 0
        penalty = customers.count('Y')

        minPenalty = penalty


        for i in range(n):
            if customers[i] == 'Y':
                penalty -= 1

            else:
                penalty += 1

            if penalty < minPenalty:
                minPenalty = penalty
                minHour = i + 1


        return minHour












