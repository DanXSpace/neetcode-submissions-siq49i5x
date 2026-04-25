class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_nums = []

        for num in nums:
            if num in set_nums:
                return True 
            set_nums.append(num)
        return False