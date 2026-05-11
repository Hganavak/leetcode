class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        smallest = math.inf

        l = 0
        r = len(nums) - 1


        while l < r:
            mid = (l + r) // 2
            print(f"{l=}, {r=}, {mid=}, {smallest=}, {nums[mid]=}")

            smallest = min(smallest, nums[mid])

            if nums[mid] > nums[r]:
                print("\tl")
                l = mid + 1
            else:
                print("\tr")
                r = mid

        print(f"Final {smallest=}")
        return nums[l]



        