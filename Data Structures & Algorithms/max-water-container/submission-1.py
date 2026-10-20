class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        max_area=0
        while i<j:
            width=j-i
            current_area=(j-i)*min(heights[i],heights[j])
            if current_area > max_area :
                max_area=current_area
            if heights[i]>=heights[j]:
                j-=1
            else:
                i+=1
        return max_area        
                