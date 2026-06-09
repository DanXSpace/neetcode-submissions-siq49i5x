class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        res = 0

        slow, fast = 0, 1

        while fast < len(nums):
            if nums[slow] != nums[fast]:
                slow += 1
                fast += 1
            else:
                res = nums[slow]
                break
        return res