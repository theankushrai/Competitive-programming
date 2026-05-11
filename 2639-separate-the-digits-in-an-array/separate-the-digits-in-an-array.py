class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        
        def separate(num):
            result=[]
            num=str(num)
            for ch in num:
                result.append(int(ch))
            return result

        result=[]
        for it in nums:
            result.extend(separate(it))
        
        return result