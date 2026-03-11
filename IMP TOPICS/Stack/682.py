class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stck = []
        total = 0

        for i in operations:
            if i == '+':
                val = stck[-1]+ stck[-2]
                stck.append(val)
                total += val

            elif i == 'D':
                val = 2*stck[-1]
                stck.append(val)
                total += val


            elif i == 'C':
                total -= stck.pop()


            else:
                val = int(i)
                stck.append(val)
                total += val


        return total