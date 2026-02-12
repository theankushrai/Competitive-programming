class Solution:
    def longestBalanced(self, s: str) -> int:

        def is_same_freq(char_count):
            first_element_count= next(iter(char_count.values()))
            for el,count in char_count.items():
                if count!=first_element_count:
                    return False
            return True
        result_count=0
        n=len(s)
        for i in range(n):
            char_count=defaultdict(int)
            for j in range(i,n):
                char_count[s[j]]+=1
                if is_same_freq(char_count):
                    result_count=max(result_count,j-i+1)
        
        return result_count
