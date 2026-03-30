class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=""
        
        for word in strs:
            encoded += f"{len(word)}#{word}"

        return encoded


    def decode(self, s: str) -> List[str]:
        decoded = []

        i=0

        while i < len(s):

            # Make a second pointer, and keep going untit we find the #
            j=i

            while j < len(s) and s[j] != "#":
                j += 1

            # The number of chars is the chars between i and j (substring)
            length=int(s[i:j])

            # Append chars from j+1 (after the hash), up to length characters
            decoded.append(s[j+1:j+1+length])


            # Then jump i up to the end of the character we just added
            i = j + 1 + length

        return decoded


