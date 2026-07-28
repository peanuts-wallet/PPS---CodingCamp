# A101 Fair Candy Swap
from typing import List


class Solution:
    def fairCandySwap(
        self,
        aliceSizes: List[int],
        bobSizes: List[int]
    ) -> List[int]:

        alice_total = sum(aliceSizes)
        bob_total = sum(bobSizes)

        difference = (alice_total - bob_total) // 2
        bob_set = set(bobSizes)

        for alice_candy in aliceSizes:
            bob_candy = alice_candy - difference

            if bob_candy in bob_set:
                return [alice_candy, bob_candy]

