class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        count = {}
        
        for a, b in edges:
            count[a] = count.get(a, 0) + 1
            count[b] = count.get(b, 0) + 1
        
        for node in count:
            if count[node] == len(edges):
                return node
