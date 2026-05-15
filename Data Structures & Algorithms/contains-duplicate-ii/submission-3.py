class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # [1,2,3,1] k = 3

        window = set()
        left = 0

        for right in range(len(nums)):
            if abs(left - right) > k:
                window.remove(nums[left])
                left += 1
            if nums[right] in window:
                return True
            window.add(nums[right])
        return False