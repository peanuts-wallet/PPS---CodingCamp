class Solution:
    def fairCandySwap(self, aliceSizes: list[int], bobSizes: list[int]) -> list[int]:
        alice_total = sum(aliceSizes)
        bob_total = sum(bobSizes)
        
        diff = (alice_total - bob_total) // 2
        
        bob_set = set(bobSizes)
        
        for alice in aliceSizes:
            bob = alice - diff
            
            if bob in bob_set:
                return [alice, bob]