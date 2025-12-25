class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse = True)

        total = 0
        dec = 0

        for i in range(k):
            val = happiness[i] - dec

            if val <= 0:
                break

            dec += 1
            total += val

        return total
