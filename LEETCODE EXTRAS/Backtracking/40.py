class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def solve(curr, target, candidates,idx):
            if target == 0:
                result.append(curr)
            
            if target<0:
                return
            
            for i in range(idx,len(candidates)):
                #Skip Duplicates
                if i>idx and candidates[i] == candidates[i-1]:
                    continue
                solve(curr+[candidates[i]],target-candidates[i],candidates,i+1)
            return


        solve([],target,candidates,0)

        return result
    
    '''
    Appraoch: Backtracking Combination Sum - Take Reference from LEETCODE #216
    '''