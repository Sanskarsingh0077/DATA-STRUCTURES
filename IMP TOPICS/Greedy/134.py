class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        '''
        # What question wants?


        - Given n ciruclar gas sations
        - Given arr gas[....] and costs[...]
        - gas[i] == amount of gas at ith station
        - cost[i] == amount of gas needed to travel from i ---> i + 1

        - Have car that store unlimited gas, begining with empty car
        - Return i station such that all stations are visited once clockwise

        - If possible return i else return -1


        total = gas[i] - cost[i]

        
        Ex : 1                      Ex: 2 [1,2,3] [2,3,2]
                                          [1-2] = -1
        [1-2] = -1                        [2-3] = -1
        [2-2] = 0                         [3-2] = 1
        [3-4] = 0
        [4-1] = 3   

        3 - 1 = 2                           -1 + -1 + 1 = -1(not possible)

        '''
        # Greedy O(n)
        if sum(gas) < sum(cost):
            return -1

        total = 0
        index = 0

        for i in range(len(gas)):
            total += gas[i] - cost[i]

            if total < 0:
                total = 0
                index = i + 1

        return index