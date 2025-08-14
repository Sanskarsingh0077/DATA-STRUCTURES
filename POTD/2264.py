def largestGoodInteger(self, num: str) -> str:
        maxstr = ' '
        for i in range(2,len(num)):
            if num[i] == num[i-1] and num[i] == num[i-2]:
                maxstr = max(maxstr, num[i])
                

        if maxstr == ' ':
            return ""

        return maxstr * 3