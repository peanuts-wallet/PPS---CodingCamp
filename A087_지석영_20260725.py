# A087 Maximum Units on a Truck
from typing import List


class Solution:
    def maximumUnits(
        self,
        boxTypes: List[List[int]],
        truckSize: int
    ) -> int:

        boxTypes.sort(key=lambda box: box[1], reverse=True)

        answer = 0

        for box_count, units_per_box in boxTypes:
            loaded_boxes = min(box_count, truckSize)

            answer += loaded_boxes * units_per_box
            truckSize -= loaded_boxes

            if truckSize == 0:
                break

        return answer

