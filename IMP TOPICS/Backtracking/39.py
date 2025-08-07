class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def solve(curr, target, candidates, idx):
            if target == 0:
                result.append(curr)
                return
            
            if target < 0:
                return
            
            for i in range(idx,len(candidates)):
                solve(curr+[candidates[i]],target-candidates[i],candidates,i)
            return


        solve([], target , candidates, 0)

        return result
    
    '''
    Apprach: Similar to 216. Take it as reference.
    '''