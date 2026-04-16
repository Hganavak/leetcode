class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l, r = 0, 0

        count = {} # Frequency map
        b = 0

        for r in range(len(s)):
            print(f"{count=}, {b=}, {r=}")

            count[s[r]] = 1 + count.get(s[r], 0)

            if ((r - l) + 1)  - max(count.values()) > k:
                
                count[s[l]] -= 1
                l += 1

            b = max(b, (r-l) + 1)

        return b
