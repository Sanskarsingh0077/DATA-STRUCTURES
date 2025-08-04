def totalFruit(self, fruits: List[int]) -> int:
        fruitsmp = {}
        max_fruits = 0
        start = 0

        for end in range(len(fruits)):
            if fruits[end] not in fruitsmp: # create map to store every fruits and its frequency.
                fruitsmp[fruits[end]] = 0

            fruitsmp[fruits[end]] += 1

            while len(fruitsmp) > 2: # Remove more than two keys in map
                fruitsmp[fruits[start]] -= 1
                if fruitsmp[fruits[start]] == 0:
                    del fruitsmp[fruits[start]]
                
                start += 1  # shrink window from left

            max_fruits = max(max_fruits, (end - start)+1)

        return max_fruits