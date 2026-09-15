class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize != 0:
            return False
        
        sortedHand = sorted(hand)

        freq_map = Counter(sortedHand)

        for num in freq_map:
            if freq_map[num] > 0:
                count = freq_map[num]
                for i in range(groupSize):
                    next_card = num + i
                    if freq_map[next_card] < count:
                        return False
                    freq_map[next_card] -= count
        return True
            