class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        b = 1

        l, r = 0, 1
        substring = set(s[l])

        while r < len(s):
            print(f"{substring=}, {b=}, {l=}, {r=}")

            if s[r] not in substring:
                print(f"\t{s[r]=} not in substring")
                substring.add(s[r])
                b = max(len(substring), b)

            else:
                print(f"\t{s[r]=} already in substring")
                while s[r] in substring:
                    print('\t\tmomving l until we find and remove it')
                    substring.remove(s[l])
                    l += 1
                
                substring.add(s[r])
                # l += 1
            
            r += 1






        return b
        