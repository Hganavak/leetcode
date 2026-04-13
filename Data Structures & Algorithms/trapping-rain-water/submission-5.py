class Solution:
    def trap(self, height: List[int]) -> int:
        # max=0
       # For each column x

        # burst = false
        # while not burst:

            # Start at height i=0
            # If its filled
                # increase i

            # Else
                # l=x-1 until we find sommething same height
                # r=x+1 until we find sommething same height

                # if l == 0 or r == len(height)
                    # burst = true

                # else:
                    # i += 1
                    # max += 1
        
        # return max

        area = 0
        for x in range(len(height)):
            # print(f"{x=}")

            burst = False
            i = height[x] + 1

            # print(f"{i=}, {area=}")


            while not burst:


                l = x - 1
                r = x + 1
                left_wall_found = False;
                right_wall_found = False;

                # print(f"\t{l=}, {r=}, {left_wall_found=}, {right_wall_found=}")

                while not left_wall_found and not burst:
                    # print(f"\t\t{l=}")
                    if l < 0:
                        # print('\t\tleft_wall burst')
                        burst = True
                    elif height[l] >= i:
                        # print('\t\tleft_wall found')
                        left_wall_found = True

                    l -= 1

                while not right_wall_found and not burst:
                    # print(f"\t\t{r=}")
                    if r >= len(height):
                        # print('\t\tright_wall burst')
                        burst = True
                    elif height[r] >= i:
                        # print('\t\tright_wall found')
                        right_wall_found = True

                    r += 1

                if left_wall_found and right_wall_found:
                    area += 1
                    i += 1

        return area






        