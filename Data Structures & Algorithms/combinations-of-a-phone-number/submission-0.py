class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combs = []
        curCombs = ""

        digit_mapping = {"2": "abc",
                         "3": "def",
                         "4": "ghi",
                         "5": "jkl",
                         "6": "mno",
                         "7": "pqrs",
                         "8": "tuv",
                         "9": "wxyz"}

        def backtrack(i, curCombs):
            if len(curCombs) == len(digits):
                combs.append(curCombs)
                return

            for c in digit_mapping[digits[i]]:
                backtrack(i + 1, curCombs + c)

        if digits:
            backtrack(0, curCombs)

        return combs

        