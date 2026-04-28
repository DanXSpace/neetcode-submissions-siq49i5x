class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # [2,20,10,3,4,5]
        # cur_num = 5
        # cur_len = 4

        set_nums = set(nums)

        res = 0

        for num in set_nums:
            if num - 1 in set_nums:
                continue
            
            cur_num = num
            cur_len = 1

            while cur_num + 1 in set_nums:
                cur_num += 1
                cur_len += 1
            
            res = max(res, cur_len)
        return res