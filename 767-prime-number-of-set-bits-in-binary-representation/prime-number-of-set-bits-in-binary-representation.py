class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        is_prime=set([2,3,5,7,11,13,17,19,23,29,31])
        result=0
        for i in range(left,right+1):
            if (bin(i).count('1')) in is_prime:
                result+=1
        
        return result
