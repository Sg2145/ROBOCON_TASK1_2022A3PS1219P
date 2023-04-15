class Solution(object):
    def constructRectangle(self, area):
        width = int(math.sqrt(area))
        length=area // width
        while area % width != 0:
            width -= 1
            length = area // width
        return [length, width]
