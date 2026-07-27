
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)

        answer = 0

        for boxes, units in boxTypes:
            take = min(boxes, truckSize)
            answer += take * units
            truckSize -= take

            if truckSize == 0:
                break

        return answer