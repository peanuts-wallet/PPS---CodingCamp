class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        flag = 0
        count = 0
        target = edges[0][0]
        for edge in edges:
                if target in edge:
                    count += 1
        if count == len(edges): flag = 1
        if flag == 0: target = edges[0][1]
        return target