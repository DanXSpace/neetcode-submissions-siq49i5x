class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets, curset = [], []
        nums.sort()

        def backtrack(i, nums, subsets, curset):

            if i >= len(nums):
                subsets.append(curset.copy())
                return
            

            # decision to add nums[i]
            curset.append(nums[i])
            backtrack(i + 1, nums, subsets, curset)
            curset.pop()

            # decision to not add nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                 i += 1
            backtrack(i + 1, nums, subsets, curset)

        backtrack(0, nums, subsets, curset)
        return subsets
