class Solution:
    def addBinary(self, a: str, b: str) -> str:
        total = 0
        carry = 0

        m = len(a) - 1
        n = len(b) - 1

        res = ""

        while m >= 0 or n >= 0 or carry:
            total = carry
            if m >= 0:
                total += int(a[m])
                m -= 1

            if n >= 0:
                total += int(b[n])
                n -= 1

            res += str(total % 2)
            carry = total // 2

        return res[::-1]

            