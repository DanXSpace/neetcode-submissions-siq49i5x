class Solution:
    def rob(self, nums: List[int]) -> int:
       # dp[i]  = max(dp[i -1], nums[i] + dp[n-1])

       n = len(nums)

       if n == 0: return 0
       if n == 1: return nums[0]

       dp = [0] * n

       prev2 = nums[0]
       prev1 = max(nums[0], nums[1])

    

       for i in range(2, n):
            current = max(prev1, prev2 + nums[i])

            prev2 = prev1
            prev1 = current

       return prev1