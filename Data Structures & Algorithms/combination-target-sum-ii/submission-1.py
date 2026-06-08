class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        combs, curComb = [], []

        def backtrack(i , candidates, target, combs, curComb):

            if sum(curComb) == target:
                combs.append(curComb.copy())
                return
            
            if i == len(candidates) or sum(curComb) > target:
                return
            
            # decision to add candidates[i]
            curComb.append(candidates[i])
            backtrack(i + 1, candidates, target, combs, curComb)
            curComb.pop()

            # decision to not add candidates[i]
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            
            backtrack(i + 1, candidates, target, combs, curComb)

        backtrack(0, candidates, target, combs, curComb)
        return combs