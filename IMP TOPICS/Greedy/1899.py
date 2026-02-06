class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good= set()

        for a, b, c in triplets:
            if a <= target[0] and b <= target[1] and c <= target[2]:
                if a == target[0]:
                    good.add(0)

                if b == target[1]:
                    good.add(1)

                if c == target[2]:
                    good.add(2)


        return len(good) == 3


    '''

    Algorithm:
        1.	Initialize an empty set good to track which target indices (0, 1, 2) are achievable.
        2.	Iterate through each triplet (a, b, c) in triplets.
        3.	Skip the triplet if any value is greater than the corresponding value in target.
        4.	For a valid triplet:
            •	If a == target[0], mark index 0 as achievable.
            •	If b == target[1], mark index 1 as achievable.
            •	If c == target[2], mark index 2 as achievable.
        5.	After processing all triplets, return True if all three indices {0, 1, 2} are marked; otherwise return False.
        
    '''
                    