class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)

        count = 0

        for num in set_nums:
            if num - 1 in set_nums:
                continue
            
            cur_num = num
            cur_len = 1

            while cur_num + 1 in set_nums:
                cur_num += 1
                cur_len += 1

            count = max(count, cur_len)
        return count
