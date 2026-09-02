class Solution:
    def countGoodRectangles(self, rectangles: list[list[int]]) -> int:
        square_sides = [min(length, width) for length, width in rectangles]
        largest_side = max(square_sides)

        return square_sides.count(largest_side)
