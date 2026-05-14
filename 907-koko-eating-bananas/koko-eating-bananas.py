class Solution:
    def minEatingSpeed(self, nums: List[int], h: int) -> int:

        def hours_needed(k): # k  = Banana per hour
            ans=0
            for it in nums:
                ans+=math.ceil(it/k)
            return ans

        start=1
        end= max(nums)
        mink = float('inf')
        while start<=end: #find k 
            mid=(start+end)//2
            result=hours_needed(mid)
            if result<=h:
                mink=min(mink,mid)
                end=mid-1
            else :
                start=mid+1
        
        return mink
