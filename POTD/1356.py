class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        binary_array = [bin(i) for i in arr]

        ones = [0]*len(arr)

        for i, n in enumerate(binary_array):
            ones[i] = (n.count('1'), arr[i])

        
        res = [n for i, n in sorted(ones, key = lambda x : (x[0], x[1]))]

        return res


        


