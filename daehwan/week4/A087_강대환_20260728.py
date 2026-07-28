class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        answer = 0
        
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        
        for box, unit in boxTypes:
            if truckSize >= box:
                answer += box * unit
                truckSize -= box
            else:
                answer += truckSize * unit
                break
        
        return answer