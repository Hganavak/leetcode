class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded=""
        for word in strs:
            encoded += f"{len(word)}#{word}"

        # print('Encoded: ', encoded)
        return encoded


    def decode(self, s: str) -> List[str]:
        decoded = []
        # print('s: ', s)

        i=0

        while i < len(s):
            # print('\tdecoded: ', decoded)
            # print('\ti: ', i, 's[i]: ', s[i])

            j=i

            while j < len(s) and s[j] != "#":
                # print('\t\tj:', j)
                j += 1

            length=int(s[i:j])
            # print('\t\tTherefore length=', length)


            decoded.append(s[j+1:j+1+length])


            i = j + 1 + length

        return decoded


