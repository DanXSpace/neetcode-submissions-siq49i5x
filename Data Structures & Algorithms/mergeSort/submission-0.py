# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        def helperSort(pairs, s, e):
            if e - s + 1 <= 1:
                return
            
            # find the middle m
            m = (s+e) // 2

            # sort the left half
            helperSort(pairs, s, m)

            # sort. the right half
            helperSort(pairs, m + 1, e)

            # merge the sorted halves
            merge(pairs, s, m, e)
            return

        def merge(pairs, s, m, e):
            # copy the sorted left and right halfs to temp arrays
            L = pairs[s: m + 1]
            R = pairs[m + 1: e + 1]

            i = 0 # index for left
            j = 0 # idnex for right
            k = s # index for arr

            # merge two sorted halfs into the original array
            while i < len(L) and j < len(R):
                if L[i].key <= R[j].key:
                    pairs[k] = L[i]
                    i += 1
                else:
                    pairs[k] = R[j]
                    j += 1
                k += 1

            # one of the halfs will have elements remaining
            while i < len(L):
                pairs[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                pairs[k] = R[j]
                j += 1
                k += 1
        helperSort(pairs, 0, len(pairs)-1)
        return pairs

            