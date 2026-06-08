class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subSets, curSet = [], []

        def helper(i, nums, curSet, subSets):
            if i == len(nums):
                subSets.append(curSet.copy())
                return
            
            # decision to add nums[i]
            curSet.append(nums[i])
            helper(i + 1, nums, curSet, subSets)
            curSet.pop()

            # decision to not add nums[i]
            helper(i + 1, nums, curSet, subSets)

        helper(0, nums, curSet, subSets)
        return subSets
            

            