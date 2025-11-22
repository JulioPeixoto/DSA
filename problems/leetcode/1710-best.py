class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        totalUnits = 0
        for numberOfBoxes, unitsPerBox in boxTypes:
            if truckSize == 0:
                break
            take = min(numberOfBoxes, truckSize)
            totalUnits += take * unitsPerBox
            truckSize -= take
        return totalUnits

