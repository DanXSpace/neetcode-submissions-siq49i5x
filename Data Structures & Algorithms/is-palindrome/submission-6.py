class Solution:
    def isPalindrome(self, s: str) -> bool:
        # "Was it a car or a cat I saw?"
        # l = a
        # r = a

        cleaned_s = []
        for c in s:
            if c.isalnum():
                cleaned_s.append(c.lower())
            
        s = ''.join(cleaned_s)

        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            
            left += 1
            right -= 1
        return True