class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        i=j=float('inf')

        for it in nums:
            if it<=i:
                i=it
            elif it <=j:
                j=it
            else:
                return True
        
        return False