class Solution:
    def solve(self,cards):
        eps = 0.1
        if len(cards) == 1:
            return abs(cards[0] - 24.0) <= eps
        
        # Pick two possible numbers

        for i in range(len(cards)):
            for j in range(len(cards)):
                if i == j:
                    continue

                temp = []
                for k in range(len(cards)):
                    if k != i and k != j:
                        temp.append(cards[k])

                a = cards[i]
                b = cards[j]

                possibleVals = [a+b, a-b, a*b, b-a]

                if abs(b) >0:
                    possibleVals.append(a/b)

                if abs(a) > 0:
                    possibleVals.append(b/a)

                for val in possibleVals:
                    temp.append(val) #Do

                    if self.solve(temp) == True: #Explore
                        return True
                    temp.pop() #Undo
        return False

    def judgePoint24(self, cards: List[int]) -> bool:
        nums = []

        for i in range(len(cards)):
            nums.append(1.0 * cards[i])


        return self.solve(nums)