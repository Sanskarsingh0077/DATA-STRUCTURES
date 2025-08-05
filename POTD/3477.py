def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        count = 0
        used = [False] * len(baskets) 

        for fruit in fruits:
            placed = False

            for j in range(len(baskets)):
                if not used[j] and fruit <= baskets[j]:
                    used[j] = True
                    placed = True
                    break

            if not placed:
                count += 1

        return count