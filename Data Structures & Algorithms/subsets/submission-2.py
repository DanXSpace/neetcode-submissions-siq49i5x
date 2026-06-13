class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets, curSet = [], []

        def backtrack(i, nums, subsets, curSet):

            if i >= len(nums):
                subsets.append(curSet.copy()) 
                return

            # decision to add nums[i]
            curSet.append(nums[i])
            backtrack(i + 1, nums, subsets, curSet)
            curSet.pop()

            # decision to not add nums[i]
            backtrack(i + 1, nums, subsets, curSet)

        backtrack(0, nums, subsets, curSet)
        return subsets