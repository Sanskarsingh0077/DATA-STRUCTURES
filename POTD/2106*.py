def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = len(fruits)

        prefixsum = [0]*n
        positions = [0]*n

        for i in range(n):
            positions[i] = fruits[i][0]
            prefixsum[i] = fruits[i][1] + (prefixsum[i-1] if i > 0 else 0)

        
        maxFruits = 0

        for d in range((k//2) + 1):
            #Case 1 : D steps to left move

            remain = k - 2*d
            i = startPos - d
            j = startPos + remain


            left = bisect.bisect_left(positions, i)
            right = bisect.bisect_right(positions, j) -1

            if left <= right:
                total = prefixsum[right] - (prefixsum[left-1] if left > 0 else 0)

                maxFruits = max(maxFruits, total)

            # Case 2: Move D steps to right
            #remain = k - 2*d
            j = startPos + d
            i = startPos - remain

            left = bisect.bisect_left(positions, i)
            right = bisect.bisect_right(positions, j) -1

            if left <= right:
                total = prefixsum[right] - (prefixsum[left-1] if left > 0 else 0)

                maxFruits = max(maxFruits, total)


        return maxFruits