class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        p = [[0, 0, 0]]

        for ch in s:
            a, b, c = p[-1]   # unpack previous counts
        
            if ch == 'a':
                a += 1
            elif ch == 'b':
                b += 1
            else:
                c += 1
        
            p.append([a, b, c])

        ans = 0
        m = {}
        for i, (a, b, c) in enumerate(p):
            for k in [
                (-1, a - b, a - c), # a,b,c
                (-2, a - b, c),     # a,b
                (-3, b - c, a),     # b,c
                (-4, c - a, b),     # a,c
                (-5, b, c),         # a
                (-6, c, a),         # b
                (-7, a, b),         # c
            ]:
                if not k in m: m[k] = i #if signature not in map add it 
                else: ans = max(ans, i - m[k]) #else find last occurance of that signature

        return ans