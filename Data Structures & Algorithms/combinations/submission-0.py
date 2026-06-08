class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combs = []

        def helper(i, curComb, combs, n, k):
            # check if curComb == k: add that to our combs
            if len(curComb) == k:
                combs.append(curComb.copy())
                return

            # if i > n: stop
            if i > n:
                return

            # decision to add i
            curComb.append(i)
            helper(i + 1, curComb, combs, n, k)
            curComb.pop()

            # decision to not add i
            helper(i + 1, curComb, combs, n, k)
        
        helper(1, [], combs, n, k)
        return combs