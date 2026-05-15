class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        curSum = sum(arr[:k - 1])

        for left in range(len(arr) - k + 1):
            curSum += arr[left + k - 1]
            if (curSum / k ) >= threshold:
                res += 1
            curSum -= arr[left]
        return res