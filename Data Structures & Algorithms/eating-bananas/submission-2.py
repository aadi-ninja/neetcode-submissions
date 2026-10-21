import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        ans=high
        while low<=high:
            mid=(low+high)//2
            tothrs =0
            for pile in piles:
                tothrs += math.ceil(float(pile)/mid)
            if tothrs <= h:
                ans= mid
                high =mid-1
            else:
                low=mid+1
        return ans