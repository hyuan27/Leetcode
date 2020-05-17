class Solution(object):
    def maxArea(self, height):
        start = 0
        end = len(height) - 1
        area = 0
        wid = end - start
        while start < end:
            area = max(area,min(height[start],height[end])*(wid))
            if height[start] < height[end]:
                start+=1
            else:
                end -= 1
            wid -= 1 
        return area
        
