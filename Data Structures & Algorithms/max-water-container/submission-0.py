class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0 
        r=len(heights)-1
        out=0
        while l<r: 
            out=max(out,(min(heights[l],heights[r])*(r-l)))
            if heights[l]<heights[r]: 
                l+=1 
            else: 
                r-=1 
        return out 