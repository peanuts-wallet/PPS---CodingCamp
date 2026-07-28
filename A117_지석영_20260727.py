# A117 Distance Between Bus Stops
from typing import List


class Solution:
    def distanceBetweenBusStops(
        self,
        distance: List[int],
        start: int,
        destination: int
    ) -> int:

        if start > destination:
            start, destination = destination, start

        first_distance = sum(distance[start:destination])
        second_distance = sum(distance) - first_distance

        return min(first_distance, second_distance)

