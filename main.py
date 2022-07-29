class Solution(object):
    def trap(self, height):
        elevation = 0
        volume = 0
        maxHeight = max()
        while elevation < max(height):
            elevation += 1
            wall = False
            lineVolume = 0
            for count in range(len(height)):
                if height[count] >= elevation and wall is False:
                    wall = True
                    continue
                if wall is True and height[count] < elevation:
                    lineVolume += 1
                    continue
                if height[count] >= elevation and wall is True:
                    volume += lineVolume
                    lineVolume = 0
        return volume
