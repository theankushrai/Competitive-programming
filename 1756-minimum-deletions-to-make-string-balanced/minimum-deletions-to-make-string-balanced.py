class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)

        # suffix count of 'b' (including current index)
        b_suffix = [0] * n
        count_b = 0
        for i in range(n - 1, -1, -1):
            if s[i] == 'b':
                count_b += 1
            b_suffix[i] = count_b

        min_deletions = n
        a_prefix = 0

        # prefix count of 'a' (including current index)
        for i in range(n):
            if s[i] == 'a':
                a_prefix += 1

            kept = a_prefix + b_suffix[i]
            min_deletions = min(min_deletions, n - kept)

        return min_deletions