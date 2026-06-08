class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subSets, curSet = [], []

        def backtracking(i, nums, subSets, curSet):
            if i == len(nums):
                subSets.append(curSet.copy())
                return
            
            # decision to add nums[i]
            curSet.append(nums[i])
            backtracking(i + 1, nums, subSets, curSet)
            curSet.pop()

            # decision to NOT add nums[i]
            backtracking(i + 1, nums, subSets, curSet)

        backtracking(0, nums, subSets, curSet)
        return subSets

