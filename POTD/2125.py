class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        n = len(bank)

        prevDevice = 0
        res = 0

        for i in range(n):
            currDevice = 0
            for ch in bank[i]:
                if ch == '1':
                    currDevice += 1

            res += (currDevice * prevDevice)

            if currDevice != 0:
                prevDevice = currDevice

        return res