class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #=== Brute Force Approach ===#
        # if len(heights) == 2:
        #     return min(heights[0], heights[1])

        # l,r,b = 0, 1, 0

        # while l < len(heights) - 1:
        #     while r < len(heights):
        #         container_size = min(heights[l], heights[r]) * (r - l)
        #         b = max(container_size, b)
        #         r += 1

        #     l += 1
        #     r = l + 1
        
        # return b
        #=== End Brute force approach ===#

        if len(heights) == 2:
            return min(heights[0], heights[1])

        l,r,b = 0, len(heights) - 1, 0

        while l < r:
            print(f"{l=}, {r=}, {b=}")
            container_size = min(heights[l], heights[r]) * (r - l)
            print(f"{container_size=}")
            b = max(container_size, b)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return b

            
        


        

    


