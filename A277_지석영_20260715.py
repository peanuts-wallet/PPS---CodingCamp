# A277 Find Center of Star Graph
from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        first_edge = edges[0]
        second_edge = edges[1]

        if first_edge[0] == second_edge[0] or first_edge[0] == second_edge[1]:
            return first_edge[0]

        return first_edge[1]

