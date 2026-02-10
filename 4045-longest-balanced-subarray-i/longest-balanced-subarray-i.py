class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n=len(nums)
        def is_even(num):
            return num%2==0
        
        max_count=0
        for i in range(n):
            odd_set,even_set=set(),set()
            for j in range(i,n):
                curr=nums[j]
                if is_even(curr):
                    even_set.add(curr)
                else:
                    odd_set.add(curr)

                if len(odd_set)==len(even_set):
                    max_count=max(max_count,j-i+1)
                
        return max_count