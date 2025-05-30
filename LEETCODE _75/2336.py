class SmallestInfiniteSet:

    def __init__(self):
        self.nums = [True] * 1001
        self.i=1

    def popSmallest(self) -> int:
        result = self.i
        self.nums[self.i] = False

        for j in range(self.i + 1, 1001):
            if self.nums[j] == True:
                self.i = j
                break

        return result


    def addBack(self, num: int) -> None:
        self.nums[num] = True
        if num < self.i:
            self.i = num
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)


'''
Approach:

__init__()
	•	Initializes self.nums with all True (i.e., numbers 1 to 1000 are in the set).
	•	Sets self.i = 1, the smallest number initially available.

popSmallest()
	•	Returns the current smallest number i.
	•	Marks it as removed (self.nums[i] = False).
	•	Scans forward from i+1 to find the next smallest True value and updates self.i.

addBack(num)
	•	Sets self.nums[num] = True to mark it as available again.
	•	If num < self.i, updates self.i because the smallest number has changed.
'''
