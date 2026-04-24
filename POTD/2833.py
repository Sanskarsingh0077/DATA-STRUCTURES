class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        '''
        res = 0
        wildcard = 0
        for i in range(len(moves)):
            if moves[i] == 'L':
                res -= 1

            elif moves[i] == 'R':
                res += 1

            else:
                wildcard += 1

        return abs(res) + wildcard

        '''

        L = moves.count('L')
        R = moves.count('R')

        wildcard = moves.count('_')

        return abs(L-R)  + wildcard


                

