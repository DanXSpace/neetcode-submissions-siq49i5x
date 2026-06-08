class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combs = []
        curCombs = []

        def helper(i, nums, target, curCombs, combs):
            combs_sum = sum(curCombs)

            if combs_sum == target:
                combs.append(curCombs.copy())
                return

            if i >= len(nums) or combs_sum > target:
                return
            

            # decision to add nums[i]
            curCombs.append(nums[i])
            helper(i, nums, target, curCombs, combs)
            curCombs.pop()

            # decision to not add nums[i]
            helper(i + 1, nums, target, curCombs, combs)

        helper(0, nums, target, curCombs, combs)
        return combs