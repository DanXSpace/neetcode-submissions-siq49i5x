class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combs = []
        curCombs = []

        def backtracking(i, nums, target, combs, curCombs):
            if sum(curCombs) == target:
                combs.append(curCombs.copy())
                return
            
            if i == len(nums) or sum(curCombs) > target:
                return

            # decision to add nums[i]
            curCombs.append(nums[i])
            backtracking(i, nums, target, combs, curCombs)
            curCombs.pop()

            # decision to not add nums[i]
            backtracking(i + 1, nums, target, combs, curCombs)

        backtracking(0, nums, target, combs, curCombs)
        return combs


