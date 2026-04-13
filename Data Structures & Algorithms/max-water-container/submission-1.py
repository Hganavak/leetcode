class Solution:
    def maxArea(self, heights: List[int]) -> int:
       # If there's only 2 items, return container between 'em 

       # Initialise 2 pointers
       # Left = 0, right = 1, best = 0
       # While left < len(list)
       #    While right < len(list) + 1
       #    container_size = min(heights[left], heights[right]) * (right - left)
       #    best = max(container_size, best)
       # return best

        if len(heights) == 2:
            # print('Only 2 yo')
            return min(heights[0], heights[1])

        l,r,b = 0, 1, 0

        while l < len(heights) - 1:
            # print(f"{l=}")

            while r < len(heights):
                # print(f"\t{r=}")
                container_size = min(heights[l], heights[r]) * (r - l)
                # print(f"\t{container_size=}")
                b = max(container_size, b)


                r += 1



            l += 1
            r = l + 1
        
        return b

        

    


