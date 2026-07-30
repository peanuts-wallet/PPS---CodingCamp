class Solution:
    def distanceBetweenBusStops(
        self, distance: List[int], start: int, destination: int
    ) -> int:
        if start > destination:
            start, destination = destination, start

        route = sum(distance[start:destination])
        return min(route, sum(distance) - route)