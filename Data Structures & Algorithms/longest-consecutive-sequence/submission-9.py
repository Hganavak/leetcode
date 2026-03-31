class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        best=1
        nums = list(set(nums))
        nums.sort()
        print('sorted nums: ', nums)

        l=0
        r=1
        cur_count=1

        while r < len(nums):
            print()
            print('cur_count', cur_count)
            print('l', l)
            print('r', r)
            print('value at l:', nums[l])
            print('value at r:', nums[r])
            print('best:', best)

            if nums[r] == nums[l] + 1:
                cur_count += 1

                best = max(best, cur_count)
                r += 1
                l += 1
            else:
                cur_count = 1
                l = r
                r += 1


        return best