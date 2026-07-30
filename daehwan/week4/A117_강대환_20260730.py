class Solution:
    def distanceBetweenBusStops(self, distance: list[int], start: int, destination: int) -> int:
        if start > destination:
            start, destination = destination, start
        
        path1 = 0
        
        for i in range(start, destination):
            path1 += distance[i]
        
        total = sum(distance)
        path2 = total - path1
        
        return min(path1, path2)