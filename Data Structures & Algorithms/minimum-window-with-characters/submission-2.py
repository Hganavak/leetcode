class Solution:
    def minWindow(self, s: str, t: str) -> str:
        chars_to_find=t # The characters we're lookin' for

        best=""

        # Shit cases
        if len(s) == 0 or len(t) == 0 or len(t) > len(s):
            return ""

        if len(s) == 1:
            if s in list(t):
                return s

        # Find starting point
        for l in range(len(s)):
            print(f"{l=}, character: ", s[l])

            search_list=list(t)

            if s[l] in search_list: # If we find a char
                search_list.remove(s[l])

                # If we're only looking for a single char
                if len(search_list) == 0:
                    return t

                for r in range(l+1, len(s)): # Start an inner loop
                    print(f"\t{s[r]=}, character: ", search_list, f"{r=}")

                    if s[r] in search_list: # If we find a char
                        print(f"\t\t Found a matching r")
                        search_list.remove(s[r])

                        # Now check if we've found all the characters
                        if len(search_list) == 0:
                            print("\t\t\tHell yeah found 'em all")

                            new_subs = s[l:r+1]
                            print(f"\t\t\t{new_subs}")

                            if best == "" or len(new_subs) < len(best):
                                best = new_subs
                                
                            break
                            
        return best
